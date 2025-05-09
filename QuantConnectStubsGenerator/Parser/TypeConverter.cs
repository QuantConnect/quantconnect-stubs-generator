/*
 * QUANTCONNECT.COM - Democratizing Finance, Empowering Individuals.
 * Lean Algorithmic Trading Engine v2.0. Copyright 2014 QuantConnect Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
*/

using Microsoft.CodeAnalysis;
using System.Collections.Generic;
using QuantConnectStubsGenerator.Model;

namespace QuantConnectStubsGenerator.Parser
{
    /// <summary>
    /// The TypeConverter is responsible for converting AST nodes into PythonType instances.
    /// </summary>
    public class TypeConverter
    {
        private readonly SemanticModel _model;

        public TypeConverter(SemanticModel model)
        {
            _model = model;
        }

        /// <summary>
        /// Returns the symbol of the given node.
        /// Returns null if the semantic model does not contain a symbol for the node.
        /// </summary>
        public ISymbol GetSymbol(SyntaxNode node)
        {
            // ReSharper disable once ConstantNullCoalescingCondition
            return _model.GetDeclaredSymbol(node) ?? _model.GetSymbolInfo(node).Symbol;
        }

        /// <summary>
        /// Returns the Python type of the given node.
        /// Returns an aliased typing.Any if there is no Python type for the given symbol.
        /// </summary>
        public PythonType GetType(SyntaxNode node, bool skipPythonTypeCheck = false, bool skipTypeNormalization = false, bool isParameter = false)
        {
            var symbol = GetSymbol(node);

            if (symbol == null)
            {
                return node.ToFullString().Trim() switch
                {
                    "PyList" => new PythonType("List", "typing")
                    {
                        TypeParameters = new List<PythonType> {PythonType.Any}
                    },
                    "PyDict" => new PythonType("Dict", "typing")
                    {
                        TypeParameters = new List<PythonType>
                        {
                            PythonType.Any, PythonType.Any
                        }
                    },
                    _ => PythonType.Any
                };
            }

            return GetType(symbol, skipPythonTypeCheck, skipTypeNormalization, isParameter);
        }

        /// <summary>
        /// Returns the Python type of the given symbol.
        /// Returns an aliased typing.Any if there is no Python type for the given symbol.
        /// </summary>
        public PythonType GetType(ISymbol symbol, bool skipPythonTypeCheck = false, bool skipTypeNormalization = false, bool isParameter = false)
        {
            // Handle arrays
            if (symbol is IArrayTypeSymbol arrayTypeSymbol)
            {
                var listType = new PythonType("List", "typing");
                listType.TypeParameters.Add(GetType(arrayTypeSymbol.ElementType, isParameter: isParameter));
                return listType;
            }

            // Use typing.Any as fallback if there is no type information in the given symbol
            if (symbol == null || symbol.Name == "" || symbol.ContainingNamespace == null)
            {
                return PythonType.Any;
            }

            var name = GetTypeName(symbol);
            var ns = symbol.ContainingNamespace.ToDisplayString();

            var type = new PythonType(name, ns);

            // Process type parameters
            if (symbol is ITypeParameterSymbol)
            {
                type.IsNamedTypeParameter = true;
            }

            // Process named type parameters
            if (symbol is INamedTypeSymbol namedTypeSymbol)
            {
                // Process delegates
                if (namedTypeSymbol.DelegateInvokeMethod != null)
                {
                    var parameters = new List<PythonType>();

                    foreach (var parameter in namedTypeSymbol.DelegateInvokeMethod.Parameters)
                    {
                        parameters.Add(GetType(parameter.Type, isParameter: isParameter));
                    }

                    parameters.Add(GetType(namedTypeSymbol.DelegateInvokeMethod.ReturnType, isParameter: isParameter));

                    return new PythonType("Callable", "typing")
                    {
                        TypeParameters = parameters
                    };
                }

                foreach (var typeParameter in namedTypeSymbol.TypeArguments)
                {
                    var paramType = GetType(typeParameter, isParameter: isParameter);

                    if (typeParameter is ITypeParameterSymbol)
                    {
                        paramType.IsNamedTypeParameter = true;
                    }

                    type.TypeParameters.Add(paramType);
                }
            }

            var result = CSharpTypeToPythonType(type, skipPythonTypeCheck);
            if (!skipTypeNormalization)
            {
                result = NormalizeType(result, isParameter);
            }
            return result;
        }

        private string GetTypeName(ISymbol symbol)
        {
            var nameParts = new List<string>();

            var currentSymbol = symbol;
            while (currentSymbol != null)
            {
                nameParts.Add(currentSymbol.Name);
                currentSymbol = currentSymbol.ContainingType;
            }

            nameParts.Reverse();

            if (symbol is ITypeParameterSymbol typeParameterSymbol)
            {
                if (typeParameterSymbol.DeclaringMethod != null)
                {
                    nameParts.Insert(1, typeParameterSymbol.DeclaringMethod.Name);
                }
            }

            return string.Join(".", nameParts);
        }

        /// <summary>
        /// Converts a C# type to a Python type.
        /// This method handles conversions like the one from System.String to str.
        /// If the Type object doesn't need to be converted, the originally provided type is returned.
        /// </summary>
        private PythonType CSharpTypeToPythonType(PythonType type, bool skipPythonTypeCheck = false)
        {
            if (type.Namespace == "System" && !skipPythonTypeCheck)
            {
                switch (type.Name)
                {
                    case "Char":
                    case "String":
                        return new PythonType("str");
                    case "Byte":
                    case "SByte":
                    case "Int16":
                    case "Int32":
                    case "Int64":
                    case "UInt16":
                    case "UInt32":
                    case "UInt64":
                        return new PythonType("int");
                    case "Single":
                    case "Double":
                    case "Decimal":
                        return new PythonType("float");
                    case "Boolean":
                        return new PythonType("bool");
                    case "Void":
                        return new PythonType("None");
                    case "DateTime":
                        return new PythonType("datetime", "datetime");
                    case "TimeSpan":
                        return new PythonType("timedelta", "datetime");
                    case "Nullable":
                        type.Name = "Optional";
                        type.Namespace = "typing";
                        break;
                    case "Type":
                        type.Name = "Type";
                        type.Namespace = "typing";
                        break;
                }
            }

            // C# types that don't have a Python-equivalent or that we don't parse are converted to an aliased Any
            if (type.Namespace == "<global namespace>")
            {
                return new PythonType("Any", "typing")
                {
                    Alias = type.Name.Replace('.', '_')
                };
            }

            return type;
        }

        private static PythonType NormalizeType(PythonType type, bool isParameter)
        {
            var isList = false;
            var isGeneric = false;
            if (type.Namespace == "System.Collections.Generic" && type.TypeParameters.Count == 1)
            {
                isGeneric = true;

                if (type.Name == "IReadOnlyList" || type.Name == "IReadOnlyCollection")
                {
                    if (!isParameter)
                    {
                        return new PythonType("Sequence", "typing")
                        {
                            TypeParameters = { NormalizeType(type.TypeParameters[0], isParameter) }
                        };
                    }
                    isList = true;
                }
                else if (type.Name == "IList" || type.Name == "List")
                {
                    if (!isParameter)
                    {
                        return new PythonType("List", "typing")
                        {
                            TypeParameters = { NormalizeType(type.TypeParameters[0], isParameter) }
                        };
                    }
                    isList = true;
                }
                else if (type.Name == "IEnumerable")
                {
                    if (!isParameter)
                    {
                        return new PythonType("Iterable", "typing")
                        {
                            TypeParameters = { NormalizeType(type.TypeParameters[0], isParameter) }
                        };
                    }
                    isList = true;
                }
            }
            else if (type.Namespace == "System.Collections" && type.Name == "IList")
            {
                isList = true;
            }

            if (isList)
            {
                if (isGeneric)
                {
                    return new PythonType("List", "typing")
                    {
                        TypeParameters = { NormalizeType(type.TypeParameters[0], isParameter) }
                    };
                }

                return new PythonType("List", "typing")
                {
                    TypeParameters = { PythonType.Any }
                };
            }

            return type;
        }
    }
}


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

using System.Collections.Generic;
using System.Linq;
using System.Xml;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using QuantConnectStubsGenerator.Model;
using QuantConnectStubsGenerator.Utility;

namespace QuantConnectStubsGenerator.Parser
{
    public class MethodParser : BaseParser
    {
        public MethodParser(ParseContext context, SemanticModel model) : base(context, model)
        {
        }

        public override void VisitMethodDeclaration(MethodDeclarationSyntax node)
        {
            VisitMethod(
                node,
                node.Identifier.Text,
                node.ParameterList.Parameters,
                _typeConverter.GetType(node.ReturnType));

            // Make the current class extend from typing.Iterable if this is an applicable GetEnumerator() method
            ExtendIterableIfNecessary(node);

            // Add __contains__ and __len__ methods to containers in System.Collections.Generic
            AddContainerMethodsIfNecessary(node);
        }

        public override void VisitConstructorDeclaration(ConstructorDeclarationSyntax node)
        {
            if (HasModifier(node, "static"))
            {
                return;
            }

            VisitMethod(node, "__init__", node.ParameterList.Parameters, new PythonType("None"));
        }

        public override void VisitDelegateDeclaration(DelegateDeclarationSyntax node)
        {
            VisitMethod(
                node,
                node.Identifier.Text,
                node.ParameterList.Parameters,
                _typeConverter.GetType(node.ReturnType));
        }

        public override void VisitIndexerDeclaration(IndexerDeclarationSyntax node)
        {
            if (ShouldSkip(node))
            {
                return;
            }

            var returnType = _typeConverter.GetType(node.Type);

            // Improve the autocomplete on data[symbol] if data is a Slice and symbol a Symbol
            // In C# this is of type dynamic, which by default gets converted to typing.Any
            // To improve the autocomplete a bit we convert it to Union[TradeBar, QuoteBar, List[Tick], Any]
            if (_currentClass?.Type.ToPythonString() == "QuantConnect.Data.Slice")
            {
                returnType = new PythonType("Union", "typing")
                {
                    TypeParameters =
                    {
                        new PythonType("TradeBar", "QuantConnect.Data.Market"),
                        new PythonType("QuoteBar", "QuantConnect.Data.Market"),
                        new PythonType("List", "System.Collections.Generic")
                        {
                            TypeParameters = {new PythonType("Tick", "QuantConnect.Data.Market")}
                        },
                        new PythonType("Any", "typing")
                    }
                };
            }

            if (returnType.Namespace == "System" && returnType.Name == "Object")
            {
                returnType = new PythonType("Any", "typing");
            }

            VisitMethod(node, "__getitem__", node.ParameterList.Parameters, returnType);

            var symbol = _typeConverter.GetSymbol(node);
            if (symbol is IPropertySymbol propertySymbol && !propertySymbol.IsReadOnly)
            {
                VisitMethod(node, "__setitem__", node.ParameterList.Parameters, new PythonType("None"));

                var valueParameter = new Parameter("value", returnType);
                _currentClass.Methods.Last().Parameters.Add(valueParameter);
            }
        }

        private void VisitMethod(
            MemberDeclarationSyntax node,
            string name,
            SeparatedSyntaxList<ParameterSyntax> parameterList,
            PythonType returnType)
        {
            if (_currentClass == null || ShouldSkip(node))
            {
                return;
            }

            // Some methods in the AST have parameters without names
            // Because these parameters cause syntax errors in the generated Python code we skip those methods
            if (parameterList.Any(parameter => FormatParameterName(parameter.Identifier.Text) == ""))
            {
                return;
            }

            var originalReturnType = returnType;

            var method = new Method(name, returnType)
            {
                Static = HasModifier(node, "static"),
                File = _model.SyntaxTree.FilePath,
                DeprecationReason = GetDeprecationReason(node)
            };

            var doc = ParseDocumentation(node);
            if (doc["summary"] != null)
            {
                method.Summary = doc["summary"].GetText();
            }

            if (HasModifier(node, "protected"))
            {
                method.Summary = AppendSummary(method.Summary, "This method is protected.");
            }

            if (method.DeprecationReason != null)
            {
                method.Summary = AppendSummary(method.Summary, method.DeprecationReason);
            }

            var docStrings = new List<string>();
            var outTypes = new List<PythonType>();
            var hasListParameter = false;

            foreach (var parameter in parameterList)
            {
                var parsedParameter = ParseParameter(parameter);

                if (parsedParameter == null)
                {
                    continue;
                }

                foreach (XmlElement paramNode in doc.GetElementsByTagName("param"))
                {
                    if (paramNode.Attributes["name"]?.Value != parameter.Identifier.Text)
                    {
                        continue;
                    }

                    var text = paramNode.GetText();

                    if (text.Trim().Length == 0)
                    {
                        continue;
                    }

                    if (CheckDocSuggestsPandasDataFrame(text))
                    {
                        parsedParameter.Type = new PythonType("DataFrame", "pandas");
                    }

                    docStrings.Add($":param {parsedParameter.Name}: {text}");
                    break;
                }

                method.Parameters.Add(parsedParameter);

                if (parameter.Modifiers.Any(m => m.Text == "out"))
                {
                    var actualType = parsedParameter.Type;

                    // Python.NET allows passing None to out parameters
                    parsedParameter.Type = new PythonType("Optional", "typing")
                    {
                        TypeParameters = { actualType }
                    };

                    outTypes.Add(actualType);
                }

                hasListParameter |= IsListParameterType(parsedParameter.Type);
            }

            // Python.NET returns a tuple if a method has out parameters
            // The first item is the return value of the method, the following items are the out parameters
            if (outTypes.Count > 0)
            {
                var tupleType = new PythonType("Tuple", "typing");
                tupleType.TypeParameters.Add(method.ReturnType);
                outTypes.ForEach(type => tupleType.TypeParameters.Add(type));
                method.ReturnType = tupleType;
            }

            var returnsParts = new List<string>();

            if (doc["returns"] != null)
            {
                var text = doc["returns"].GetText();

                if (text.Trim().Length > 0)
                {
                    returnsParts.Add(text);
                }
            }

            if (returnsParts.Count > 0)
            {
                var parts = returnsParts.Select(part => part.EndsWith(".") ? part : part + ".");
                var text = string.Join(" ", parts);

                docStrings.Add($":returns: {text}");

                if (CheckDocSuggestsPandasDataFrame(text))
                {
                    method.ReturnType = new PythonType("DataFrame", "pandas");
                }
            }

            docStrings = docStrings.Select(str => str.Replace('\n', ' ')).ToList();

            if (docStrings.Count > 0)
            {
                var paramText = string.Join("\n", docStrings);
                method.Summary = method.Summary != null
                    ? method.Summary + "\n\n" + paramText
                    : paramText;
            }

            _currentClass.Methods.Add(method);

            ImprovePythonAccessorIfNecessary(method);

            if (hasListParameter)
            {
                method.Overload = true;

                // Generate overload methods
                var overload = new Method(method,
                    method.Parameters.Select(p => ConvertListParameter(p)).ToList())
                {
                    Overload = true
                };
                _currentClass.Methods.Add(overload);
            }
        }

        private static Parameter ConvertListParameter(Parameter parameter)
        {
            if (!IsListParameterType(parameter.Type))
            {
                return parameter;
            }

            return new Parameter(parameter)
            {
                Type = ConvertListParameterType(parameter.Type)
            };
        }

        private static PythonType ConvertListParameterType(PythonType type)
        {
            if (!IsListParameterType(type))
            {
                return type;
            }

            return new PythonType("Iterable", "typing")
            {
                TypeParameters = { ConvertListParameterType(type.TypeParameters[0]) }
            };
        }

        private static bool IsListParameterType(PythonType type)
        {
            return type.Namespace == "System.Collections.Generic" &&
                type.TypeParameters.Count == 1 &&
                (type.Name == "IReadOnlyCollection" || type.Name == "IEnumerable" || type.Name == "IList" || type.Name == "List");
        }

        private Parameter ParseParameter(ParameterSyntax syntax)
        {
            var originalName = syntax.Identifier.Text;
            var parameter = new Parameter(FormatParameterName(originalName), _typeConverter.GetType(syntax.Type));

            if (syntax.Modifiers.Any(modifier => modifier.Text == "params"))
            {
                parameter.VarArgs = true;
                parameter.Type = parameter.Type.TypeParameters[0];
            }

            // Symbol parameters can be both a Symbol or a string in most methods
            if (parameter.Type.Namespace == "QuantConnect" && parameter.Type.Name == "Symbol")
            {
                var unionType = new PythonType("Union", "typing");
                unionType.TypeParameters.Add(parameter.Type);
                unionType.TypeParameters.Add(new PythonType("str"));
                parameter.Type = unionType;
            }

            // IDataConsolidator parameters can be either IDataConsolidator, PythonConsolidator or timedelta
            if (parameter.Type.Namespace == "QuantConnect.Data.Consolidators"
                && parameter.Type.Name == "IDataConsolidator")
            {
                var unionType = new PythonType("Union", "typing");
                unionType.TypeParameters.Add(parameter.Type);
                unionType.TypeParameters.Add(new PythonType("PythonConsolidator", "QuantConnect.Python"));
                unionType.TypeParameters.Add(new PythonType("timedelta", "datetime"));
                parameter.Type = unionType;
            }

            // datetime parameters also accept dates
            if (parameter.Type.Namespace == "datetime" && parameter.Type.Name == "datetime")
            {
                var unionType = new PythonType("Union", "typing");
                unionType.TypeParameters.Add(parameter.Type);
                unionType.TypeParameters.Add(new PythonType("date", "datetime"));
                parameter.Type = unionType;
            }

            // Methods like AddData<T> and History<T> have Python implementations accepting "T" as first parameter
            // We set the types of these parameters to typing.Type instead of the default typing.Any
            if (_model.SyntaxTree.FilePath.EndsWith(".Python.cs")
                && (parameter.Name == "type" || parameter.Name == "dataType" || parameter.Name == "T"))
            {
                parameter.Type = new PythonType("Type", "typing");
            }

            // System.Object parameters can accept anything
            if (parameter.Type.Namespace == "System" && parameter.Type.Name == "Object")
            {
                parameter.Type = new PythonType("Any", "typing");
            }

            if (syntax.Default != null)
            {
                parameter.Value = FormatValue(syntax.Default.Value.ToString());
            }

            return parameter;
        }

        private string FormatParameterName(string name)
        {
            // Remove "@" prefix
            if (name.StartsWith("@"))
            {
                name = name.Substring(1);
            }

            // Escape keywords
            return name switch
            {
                "from" => "_from",
                "enum" => "_enum",
                "lambda" => "_lambda",
                _ => name
            };
        }

        private void ExtendIterableIfNecessary(MethodDeclarationSyntax node)
        {
            if (node.Identifier.Text != "GetEnumerator")
            {
                return;
            }

            if (_currentClass.InheritsFrom.Any(t => t.Namespace == "typing" && t.Name == "Iterable"))
            {
                return;
            }

            var parsedReturnType = _typeConverter.GetType(node.ReturnType);

            // Some GetEnumerator() methods return an IEnumerator, some return an IEnumerator<T>
            // typing.Iterable requires a type parameter, so we don't extend it if an IEnumerator is returned
            if (parsedReturnType.TypeParameters.Count == 0)
            {
                return;
            }

            _currentClass.InheritsFrom.Add(new PythonType("Iterable", "typing")
            {
                TypeParameters = parsedReturnType.TypeParameters
            });
        }

        private void AddContainerMethodsIfNecessary(MethodDeclarationSyntax node)
        {
            if (node.Identifier.Text != "Contains" && node.Identifier.Text != "ContainsKey")
            {
                return;
            }

            if (_currentNamespace.Name != "System.Collections.Generic")
            {
                return;
            }

            VisitMethod(node, "__contains__", node.ParameterList.Parameters, _typeConverter.GetType(node.ReturnType));

            if (_currentClass.Methods.All(m => m.Name != "__len__"))
            {
                _currentClass.Methods.Add(new Method("__len__", new PythonType("int")));
            }
        }

        /// <summary>
        /// There are several Python-friendly accessors like Slice.Get(Type) instead of Slice.Get&lt;T&gt;().
        /// If we spot such a Python-friendly accessor, we remove the non-Python-friendly accessor and improve
        /// the Python-friendly accessor's definition.
        /// </summary>
        private void ImprovePythonAccessorIfNecessary(Method newMethod)
        {
            if (newMethod.Parameters.Count != 1 || newMethod.Parameters[0].Type.ToPythonString() != "typing.Type")
            {
                return;
            }

            var existingMethod = _currentClass.Methods
                .FirstOrDefault(m => m.Name == newMethod.Name && m.Parameters.Count == 0);

            if (existingMethod == null)
            {
                return;
            }

            var typeParameter = existingMethod.ReturnType;
            while (!typeParameter.IsNamedTypeParameter && typeParameter.TypeParameters.Count > 0)
            {
                typeParameter = typeParameter.TypeParameters[0];
            }

            if (!typeParameter.IsNamedTypeParameter)
            {
                return;
            }

            newMethod.Parameters[0].Type = typeParameter;
            newMethod.ReturnType = existingMethod.ReturnType;

            _currentClass.Methods.Remove(existingMethod);
        }

        /// <summary>
        /// Returns whether the provided documentation string suggests that a certain type is a pandas DataFrame.
        /// </summary>
        private bool CheckDocSuggestsPandasDataFrame(string doc)
        {
            return doc.Contains("pandas DataFrame") || doc.Contains("pandas.DataFrame");
        }
    }
}


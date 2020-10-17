using System.Collections.Generic;
using Microsoft.CodeAnalysis;
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
        public PythonType GetType(SyntaxNode node)
        {
            var symbol = GetSymbol(node);

            if (symbol == null)
            {
                return node.ToFullString().Trim() switch
                {
                    "PyList" => new PythonType("List", "typing")
                    {
                        TypeParameters = new List<PythonType> {new PythonType("Any", "typing")}
                    },
                    "PyDict" => new PythonType("Dict", "typing")
                    {
                        TypeParameters = new List<PythonType>
                        {
                            new PythonType("Any", "typing"), new PythonType("Any", "typing")
                        }
                    },
                    _ => new PythonType("Any", "typing")
                };
            }

            return GetType(symbol);
        }

        /// <summary>
        /// Returns the Python type of the given symbol.
        /// Returns an aliased typing.Any if there is no Python type for the given symbol.
        /// </summary>
        public PythonType GetType(ISymbol symbol)
        {
            // Handle arrays
            if (symbol is IArrayTypeSymbol arrayTypeSymbol)
            {
                var listType = new PythonType("List", "typing");
                listType.TypeParameters.Add(GetType(arrayTypeSymbol.ElementType));
                return listType;
            }

            // Use typing.Any as fallback if there is no type information in the given symbol
            if (symbol == null || symbol.Name == "" || symbol.ContainingNamespace == null)
            {
                return new PythonType("Any", "typing");
            }

            var name = GetTypeName(symbol);
            var ns = symbol.ContainingNamespace.ToDisplayString();

            var type = new PythonType(name, ns);

            // Process type parameter
            if (symbol is ITypeParameterSymbol)
            {
                type.IsNamedTypeParameter = true;
            }

            // Process named type parameters
            if (symbol is INamedTypeSymbol namedTypeSymbol)
            {
                // Delegates are not supported
                if (namedTypeSymbol.DelegateInvokeMethod != null
                    && !namedTypeSymbol.DelegateInvokeMethod.ToDisplayString().StartsWith("System.Func")
                    && !namedTypeSymbol.DelegateInvokeMethod.ToDisplayString().StartsWith("System.Action"))
                {
                    return new PythonType("Any", "typing")
                    {
                        Alias = type.Namespace.Replace('.', '_') + "_" + type.Name.Replace('.', '_')
                    };
                }

                foreach (var typeParameter in namedTypeSymbol.TypeArguments)
                {
                    var paramType = GetType(typeParameter);

                    if (typeParameter is ITypeParameterSymbol)
                    {
                        paramType.IsNamedTypeParameter = true;
                    }

                    type.TypeParameters.Add(paramType);
                }
            }

            return CSharpTypeToPythonType(type);
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
            return string.Join(".", nameParts);
        }

        /// <summary>
        /// Converts a C# type to a Python type.
        /// This method handles conversions like the one from System.String to str.
        /// If the Type object doesn't need to be converted, the originally provided type is returned.
        /// </summary>
        private PythonType CSharpTypeToPythonType(PythonType type)
        {
            if (type.Namespace == "System")
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
                    case "Func":
                    case "Action":
                        if (type.TypeParameters.Count > 0)
                        {
                            type.Name = "Callable";
                            type.Namespace = "typing";
                        }

                        break;
                }
            }

            // Dictionaries
            if (type.Namespace == "System.Collections.Generic" && type.Name == "IDictionary")
            {
                type.Name = "Dict";
                type.Namespace = "typing";
            }

            // Lists
            if ((type.Namespace == "System.Collections" && type.Name == "IList")
                || (type.Namespace == "System.Collections.Generic" && type.Name == "List")
                || (type.Namespace == "System.Collections.Generic" && type.Name == "ICollection")
                || (type.Namespace == "System.Collections.Generic" && type.Name == "IEnumerable")
                || (type.Namespace == "System.Collections.Generic" && type.Name == "IReadOnlyList"))
            {
                type.Name = "List";
                type.Namespace = "typing";
            }

            // C# types that do not have a Python-equivalent are converted to an aliased version of Any
            if (type.Namespace.StartsWith("System") || type.Namespace == "<global namespace>")
            {
                var alias = type.Name.Replace('.', '_');

                if (type.Namespace.StartsWith("System"))
                {
                    alias = $"{type.Namespace.Replace('.', '_')}_{alias}";
                }

                return new PythonType("Any", "typing")
                {
                    Alias = alias
                };
            }

            return type;
        }
    }
}

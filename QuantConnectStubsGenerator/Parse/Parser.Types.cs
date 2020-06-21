using System;
using System.Collections.Generic;
using System.Diagnostics.CodeAnalysis;
using System.Linq;
using Microsoft.CodeAnalysis;
using QuantConnectStubsGenerator.Model;

namespace QuantConnectStubsGenerator.Parse
{
    public partial class Parser
    {
        /// <summary>
        /// Returns the Python type of the given symbol.
        /// Returns Any if there is no Python type for the given symbol.
        /// Also marks the type, including any type arguments, as used in the current top class.
        /// </summary>
        private PythonType GetType(ISymbol symbol)
        {
            var type = ParseType(symbol);
            MarkTypeUsed(type);
            return type;
        }

        /// <summary>
        /// Returns the Python type of the given node.
        /// Returns Any if there is no Python type for the given node.
        /// Also marks the type, including any type arguments, as used in the current top class.
        /// </summary>
        [SuppressMessage("ReSharper", "ConstantNullCoalescingCondition")]
        [SuppressMessage("ReSharper", "ConditionIsAlwaysTrueOrFalse")]
        private PythonType GetType(SyntaxNode node)
        {
            var symbol = _model.GetDeclaredSymbol(node) ?? _model.GetSymbolInfo(node).Symbol;
            var type = symbol != null ? ParseType(symbol) : NodeTextToPythonType(node.ToString());

            MarkTypeUsed(type);

            return type;
        }

        /// <summary>
        /// Parses a C# symbol to an object containing Python type information.
        /// </summary>
        private PythonType ParseType(ISymbol symbol)
        {
            // Handle arrays
            if (symbol is IArrayTypeSymbol arraySymbol)
            {
                var listType = new PythonType("List", "typing");
                listType.TypeParameters.Add(ParseType(arraySymbol.ElementType));
                return listType;
            }

            // Use Any as fallback
            if (symbol == null || symbol.Name == "" || symbol.ContainingNamespace == null)
            {
                return new PythonType("Any", "typing");
            }

            string name = null;
            var isNamedTypeParameter = false;

            // Check if the symbol is a type like "T" instead of "System.String"
            if (!symbol.ToDisplayString().Contains("."))
            {
                name = GetTypeParameterName((ITypeSymbol) symbol);
                isNamedTypeParameter = true;
            }

            if (name == null)
            {
                name = symbol.Name;

                // Add parent classes to the name
                var fullName = symbol.ToString();
                var fullNamespace = symbol.ContainingNamespace.ToDisplayString();
                var nameWithoutNamespace = fullName!.Replace(fullNamespace + ".", "");

                var nameIndex = nameWithoutNamespace.IndexOf(name, StringComparison.Ordinal);
                var prefix = nameIndex > 0
                    ? nameWithoutNamespace.Substring(0, nameIndex)
                    : "";

                name = prefix + name;
            }

            var ns = symbol.ContainingNamespace.ToDisplayString();

            var type = new PythonType(name, ns)
            {
                IsNamedTypeParameter = isNamedTypeParameter
            };

            if (symbol is INamedTypeSymbol namedSymbol)
            {
                foreach (var typeParameter in namedSymbol.TypeArguments)
                {
                    type.TypeParameters.Add(ParseType(typeParameter));
                }
            }

            return CSharpTypeToPythonType(type);
        }

        /// <summary>
        /// Generates a name for the type symbol.
        /// In the generated *.pyi files there may be multiple classes in a file.
        /// To prevent against clashing type parameters names this method names them Class_Method_Name.
        /// </summary>
        private string GetTypeParameterName(ITypeSymbol symbol)
        {
            var nameParts = new List<string>();

            var currentType = symbol;
            while (currentType != null)
            {
                nameParts.Add(currentType.Name);
                currentType = currentType.ContainingType;

                if (nameParts.Count == 1 && symbol is ITypeParameterSymbol typeParameterSymbol)
                {
                    var methodName = typeParameterSymbol.DeclaringMethod?.Name;

                    if (methodName != null)
                    {
                        var methodCount = _currentClass.Methods.Count(method => method.Name == methodName);
                        nameParts.Add($"{methodCount + 1}");
                        nameParts.Add(typeParameterSymbol.DeclaringMethod.Name);
                    }
                }
            }

            nameParts.Reverse();
            return string.Join("_", nameParts);
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
                        type.IsNamedTypeParameter = false;
                        break;
                    case "Func":
                        type.Name = "Callable";
                        type.Namespace = "typing";
                        type.IsNamedTypeParameter = false;
                        break;
                }
            }

            // IEnumerable<KeyValuePair<K, V>>
            if (type.Namespace == "System.Collections.Generic"
                && type.Name == "IEnumerable"
                && type.TypeParameters.Count == 1
                && type.TypeParameters[0].Namespace == "QuantConnect"
                && type.TypeParameters[0].Name == "KeyValuePair")
            {
                type.Name = "Dict";
                type.Namespace = "typing";
                type.TypeParameters = type.TypeParameters[0].TypeParameters;
                type.IsNamedTypeParameter = false;
            }

            // Dictionaries
            if (type.Namespace == "System.Collections.Generic" && type.Name == "IDictionary")
            {
                type.Name = "Dict";
                type.Namespace = "typing";
                type.IsNamedTypeParameter = false;
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
                type.IsNamedTypeParameter = false;
            }

            // KeyValuePair
            if (type.Namespace == "System.Collections.Generic" && type.Name == "KeyValuePair")
            {
                type.Namespace = "QuantConnect";
            }

            // C# types that do not have a Python-equivalent are converted to an aliased version of Any
            if (type.Namespace.StartsWith("System") || type.Namespace == "<global namespace>")
            {
                var alias = type.Name;

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

        /// <summary>
        /// Attempts to convert the text of a node to a Python type.
        /// If it is unable to convert the given type, the result of ParseType(null) is returned.
        /// </summary>
        private PythonType NodeTextToPythonType(string text)
        {
            PythonType type = null;

            switch (text)
            {
                case "PyList":
                    type = new PythonType("List", "typing");
                    type.TypeParameters.Add(new PythonType("Any", "typing"));
                    break;
                case "PyDict":
                    type = new PythonType("Dict", "typing");
                    type.TypeParameters.Add(new PythonType("Any", "typing"));
                    type.TypeParameters.Add(new PythonType("Any", "typing"));
                    break;
            }

            return type ?? ParseType(null);
        }

        /// <summary>
        /// Marks the given type and all of its type arguments as used in the current top class.
        /// </summary>
        private void MarkTypeUsed(PythonType type)
        {
            _topClass.UsedTypes.Add(type);

            if (type.IsNamedTypeParameter)
            {
                _currentNamespace.TypeParameterNames.Add(type.Name);
                _topClass.UsedTypes.Add(new PythonType("TypeVar", "typing"));
            }

            if (type.Alias != null)
            {
                _currentNamespace.TypeAliases.Add(new TypeAlias(type.Alias, type));
            }

            foreach (var typeParameter in type.TypeParameters)
            {
                MarkTypeUsed(typeParameter);
            }
        }
    }
}

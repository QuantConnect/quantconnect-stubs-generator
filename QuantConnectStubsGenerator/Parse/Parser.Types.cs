using System;
using System.Collections.Generic;
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

            // Mark all types in type and its type parameters as used in the current top class
            var typeQueue = new Queue<PythonType>();
            typeQueue.Enqueue(type);

            while (typeQueue.Count > 0)
            {
                var currentType = typeQueue.Dequeue();

                _topClass.UsedTypes.Add(currentType);

                if (currentType.IsNamedTypeParameter)
                {
                    _currentNamespace.TypeParameterNames.Add(currentType.Name);
                    _topClass.UsedTypes.Add(new PythonType("TypeVar", "typing"));
                }

                if (currentType.Alias != null)
                {
                    _currentNamespace.TypeAliases.Add(new TypeAlias(currentType.Alias, currentType));
                }

                foreach (var typeParameter in currentType.TypeParameters)
                {
                    typeQueue.Enqueue(typeParameter);
                }
            }

            return type;
        }

        /// <summary>
        /// Returns the Python type of the given node.
        /// Returns Any if there is no Python type for the given node.
        /// Also marks the type, including any type arguments, as used in the current top class.
        /// </summary>
        private PythonType GetType(SyntaxNode node)
        {
            return GetType(_model.GetDeclaredSymbol(node) ?? _model.GetSymbolInfo(node).Symbol);
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

            // Dictionaries
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
    }
}

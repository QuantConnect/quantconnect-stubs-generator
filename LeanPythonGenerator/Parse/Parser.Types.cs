using System.Collections.Generic;
using LeanPythonGenerator.Model;
using Microsoft.CodeAnalysis;

namespace LeanPythonGenerator.Parse
{
    public partial class Parser
    {
        /// <summary>
        /// Returns the Python type of the given symbol.
        /// Returns Any if there is no Python type for the given symbol.
        /// Also marks the type, including any type arguments, as used in the current namespace.
        /// </summary>
        private PythonType GetType(ISymbol symbol)
        {
            var type = ParseType(symbol);

            // Mark all types in type and its type parameters as used in the current namespace
            var typeQueue = new Queue<PythonType>();
            typeQueue.Enqueue(type);

            while (typeQueue.Count > 0)
            {
                var currentType = typeQueue.Dequeue();

                _currentNamespace.UsedTypes.Add(currentType);

                if (currentType.IsNamedTypeParameter)
                {
                    _currentNamespace.TypeParameterNames.Add(currentType.Name);
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
        /// Also marks the type, including any type arguments, as used in the current namespace.
        /// </summary>
        private PythonType GetType(SyntaxNode node)
        {
            return GetType(_model.GetDeclaredSymbol(node));
        }

        /// <summary>
        /// Parses a C# symbol to an object containing Python type information.
        /// </summary>
        private PythonType ParseType(ISymbol symbol, string typeParameterName = null)
        {
            // Use Any as fallback
            if (symbol == null || symbol.Name == "" || symbol.ContainingNamespace == null)
            {
                return new PythonType("Any", "typing");
            }

            var name = typeParameterName ?? symbol.Name;
            var ns = symbol.ContainingNamespace.ToDisplayString();

            var type = new PythonType(name, ns)
            {
                IsNamedTypeParameter = typeParameterName != null
            };

            if (symbol is INamedTypeSymbol namedSymbol)
            {
                foreach (var typeParameter in namedSymbol.TypeArguments)
                {
                    // Check if the type parameter is a type like "String" instead of "T"
                    if (typeParameter.ToDisplayString().Contains("."))
                    {
                        type.TypeParameters.Add(ParseType(typeParameter));
                    }
                    else
                    {
                        var parameterName = GetTypeParameterName(typeParameter);
                        type.TypeParameters.Add(ParseType(typeParameter, parameterName));
                    }
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
            // Primitives
            if (type.Namespace == "System")
            {
                switch (type.Name)
                {
                    case "String":
                        return new PythonType("str");
                    case "Int16":
                    case "Int32":
                    case "Int64":
                        return new PythonType("int");
                    case "Single":
                    case "Double":
                        return new PythonType("float");
                    case "Boolean":
                        return new PythonType("bool");
                }
            }

            // Lists
            if ((type.Namespace == "System.Collections.Generic" && type.Name == "IEnumerable")
                || (type.Namespace == "System.Collections" && type.Name == "IList")
                || (type.Namespace == "System.Collections.Generic" && type.Name == "List"))
            {
                type.Name = "List";
                type.Namespace = "typing";
            }

            // KeyValuePairs
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

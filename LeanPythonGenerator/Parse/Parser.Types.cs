using System;
using System.Collections.Generic;
using LeanPythonGenerator.Model;
using Microsoft.CodeAnalysis;

namespace LeanPythonGenerator.Parse
{
    public partial class Parser
    {
        /// <summary>
        /// Parses the type of any node in the syntax tree to a Type object containing Python type information.
        /// Also marks all parsed types, including parsed type arguments, as used in the current namespace.
        /// </summary>
        private PythonType ParseType(SyntaxNode node)
        {
            return ParseType(_model.GetDeclaredSymbol(node));
        }

        /// <summary>
        /// Parses the C# symbol to a Type object containing Python type information.
        /// Also marks all parsed types, including parsed type arguments, as used in the current namespace.
        /// </summary>
        private PythonType ParseType(ISymbol symbol, string typeName = null)
        {
            // Use Any as fallback
            if (symbol == null || symbol.Name == "")
            {
                var anyType = CSharpTypeToPythonType(new PythonType("Any", "typing"));
                _currentNamespace.UsedTypes.Add(anyType);
                return anyType;
            }

            var name = typeName ?? symbol.Name;
            var ns = symbol.ContainingNamespace.ToDisplayString();

            var type = new PythonType(name, ns != "" && ns != "<global namespace>" ? ns : null);

            if (symbol is INamedTypeSymbol namedSymbol)
            {
                foreach (var typeParameter in namedSymbol.TypeArguments)
                {
                    // The type parameter is a type like "String" instead of "T" when ContainingNamespace is not null
                    if (typeParameter.ContainingNamespace != null)
                    {
                        type.TypeParameters.Add(ParseType(typeParameter));
                    }
                    else
                    {
                        var parameterName = GetTypeParameterName(typeParameter);

                        if (parameterName != "")
                        {
                            _currentNamespace.TypeParameterNames.Add(parameterName);
                        }

                        type.TypeParameters.Add(ParseType(typeParameter, parameterName));
                    }
                }
            }

            type = CSharpTypeToPythonType(type);
            _currentNamespace.UsedTypes.Add(type);

            return type;
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
        /// Converts a C# Type object to a Python one.
        /// This method handles conversions like the one from System.String to str.
        /// If the Type object doesn't need to be converted, the originally provided type is returned.
        /// </summary>
        private PythonType CSharpTypeToPythonType(PythonType type)
        {
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

            return type;
        }
    }
}

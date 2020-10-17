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
            if (_currentClass == null)
            {
                return;
            }

            VisitMethod(
                node,
                node.Identifier.Text,
                node.ParameterList.Parameters,
                _typeConverter.GetType(node.ReturnType));
        }

        public override void VisitIndexerDeclaration(IndexerDeclarationSyntax node)
        {
            VisitMethod(node, "__getitem__", node.ParameterList.Parameters, _typeConverter.GetType(node.Type));

            var symbol = _typeConverter.GetSymbol(node);
            if (symbol is IPropertySymbol propertySymbol && !propertySymbol.IsReadOnly)
            {
                VisitMethod(node, "__setitem__", node.ParameterList.Parameters, new PythonType("None"));
            }
        }

        private void VisitMethod(
            MemberDeclarationSyntax node,
            string name,
            SeparatedSyntaxList<ParameterSyntax> parameterList,
            PythonType returnType)
        {
            if (HasModifier(node, "private"))
            {
                return;
            }

            var classContainingMethod = GetClassContainingMethod(parameterList);
            if (classContainingMethod == null)
            {
                return;
            }

            var method = new Method(name, returnType)
            {
                Static = classContainingMethod.Static || HasModifier(node, "static")
            };

            var doc = ParseDocumentation(node);
            if (doc["summary"] != null)
            {
                method.Summary = doc["summary"].GetText();
            }

            if (classContainingMethod != _currentClass)
            {
                var clsName = $"{_currentClass.Type.Namespace}.{_currentClass.Type.Name}";
                method.Summary = PrefixSummary(method.Summary, $"This is an extension method defined in {clsName}.");
            }

            if (HasModifier(node, "protected"))
            {
                method.Summary = PrefixSummary(method.Summary, "This method is protected.");
            }

            var docStrings = new List<string>();

            foreach (var parameter in parameterList)
            {
                var parsedParameter = ParseParameter(parameter, method.Name);

                if (parsedParameter == null)
                {
                    continue;
                }

                foreach (XmlElement paramNode in doc.GetElementsByTagName("param"))
                {
                    if (paramNode.Attributes["name"]?.Value == parameter.Identifier.Text)
                    {
                        var text = paramNode.GetText();

                        if (text.Trim().Length == 0)
                        {
                            continue;
                        }

                        docStrings.Add($":param {parsedParameter.Name}: {text}");
                        break;
                    }
                }

                method.Parameters.Add(parsedParameter);
            }

            if (doc["returns"] != null)
            {
                var text = doc["returns"].GetText();

                if (text.Trim().Length > 0)
                {
                    docStrings.Add($":returns: {text}");
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

            classContainingMethod.Methods.Add(method);

            SetOverloadIfNecessary(classContainingMethod, method);
        }

        private Class GetClassContainingMethod(SeparatedSyntaxList<ParameterSyntax> parameterList)
        {
            if (parameterList.Count == 0)
            {
                return _currentClass;
            }

            var firstParameter = parameterList[0];
            if (firstParameter.Modifiers.All(modifier => modifier.Text != "this"))
            {
                return _currentClass;
            }

            var classType = _typeConverter.GetType(firstParameter.Type);

            // Skip extension methods on generic types
            if (classType.IsNamedTypeParameter)
            {
                return null;
            }

            if (classType.Namespace == null || !_context.HasNamespace(classType.Namespace))
            {
                return null;
            }

            var ns = _context.GetNamespaceByName(classType.Namespace);
            return ns.HasClass(classType) ? ns.GetClassByType(classType) : null;
        }

        private Parameter ParseParameter(ParameterSyntax syntax, string methodName)
        {
            // Skip the parameter which marks this method as an extension method
            if (syntax.Modifiers.Any(modifier => modifier.Text == "this"))
            {
                return null;
            }

            var originalName = syntax.Identifier.Text;
            var parameter = new Parameter(FormatParameterName(originalName), _typeConverter.GetType(syntax.Type));

            if (syntax.Modifiers.Any(modifier => modifier.Text == "params"))
            {
                parameter.VarArgs = true;
                parameter.Type = parameter.Type.TypeParameters[0];
            }

            // Symbol parameters can be both a Symbol instance or a string containing the ticker in Add* methods
            if (methodName.StartsWith("Add")
                && parameter.Type.Namespace == "QuantConnect"
                && parameter.Type.Name == "Symbol")
            {
                var unionType = new PythonType("Union", "typing");
                unionType.TypeParameters.Add(parameter.Type);
                unionType.TypeParameters.Add(new PythonType("str"));
                parameter.Type = unionType;
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

        /// <summary>
        /// Checks if the given method that has just been added to the given class is an overload.
        /// If this is the case, all necessary method instances have their overload property set to true.
        /// </summary>
        private void SetOverloadIfNecessary(Class cls, Method method)
        {
            var methodsWithSameName = cls.Methods
                .Where(m => m.Name == method.Name)
                .ToList();

            if (methodsWithSameName.Count <= 1)
            {
                return;
            }

            foreach (var m in methodsWithSameName)
            {
                m.Overload = true;
            }
        }
    }
}

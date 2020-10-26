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
            if (HasModifier(node, "private") || HasModifier(node, "internal"))
            {
                return;
            }

            if (_currentClass == null)
            {
                return;
            }

            // Some methods in the AST have parameters without names
            // Because these parameters cause syntax errors in the generated Python code we skip those methods
            if (parameterList.Any(parameter => FormatParameterName(parameter.Identifier.Text) == ""))
            {
                return;
            }

            var method = new Method(name, returnType)
            {
                Static = HasModifier(node, "static")
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
                    if (paramNode.Attributes["name"]?.Value != parameter.Identifier.Text)
                    {
                        continue;
                    }

                    var text = paramNode.GetText();

                    if (text.Trim().Length == 0)
                    {
                        continue;
                    }

                    docStrings.Add($":param {parsedParameter.Name}: {text}");
                    break;
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

            _currentClass.Methods.Add(method);

            SetOverloadIfNecessary(method);
        }

        private Parameter ParseParameter(ParameterSyntax syntax, string methodName)
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
        private void SetOverloadIfNecessary(Method method)
        {
            var methodsWithSameName = _currentClass.Methods
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
    }
}

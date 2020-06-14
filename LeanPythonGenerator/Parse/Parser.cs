using System.Collections.Generic;
using System.Linq;
using System.Xml;
using LeanPythonGenerator.Model;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;

namespace LeanPythonGenerator.Parse
{
    public class Parser : CSharpSyntaxWalker
    {
        private readonly ParseContext _context;
        private readonly SemanticModel _model;

        private Namespace _currentNamespace;

        private Class _currentClass;

        /// <summary>
        /// If _currentClass is A.B.C then _topClass is A.
        /// </summary>
        private Class _topClass;

        public Parser(ParseContext context, SemanticModel model)
        {
            _context = context;
            _model = model;
        }

        public override void VisitNamespaceDeclaration(NamespaceDeclarationSyntax node)
        {
            _currentNamespace = _context.GetNamespaceByName(node.Name.ToString());

            base.VisitNamespaceDeclaration(node);

            _currentNamespace = null;
        }

        public override void VisitClassDeclaration(ClassDeclarationSyntax node)
        {
            if (node.Modifiers.Any(modifier => modifier.Text == "private"))
            {
                return;
            }

            var cls = _currentClass == null
                ? _currentNamespace.GetClassByType(ParseType(node))
                : new Class(ParseType(node));

            EnterClass(cls);

            CheckForClassSummary(node);

            base.VisitClassDeclaration(node);

            ExitClass();
        }

        public override void VisitStructDeclaration(StructDeclarationSyntax node)
        {
            if (node.Modifiers.Any(modifier => modifier.Text == "private"))
            {
                return;
            }

            EnterClass(new Class(ParseType(node)));

            CheckForClassSummary(node);

            base.VisitStructDeclaration(node);

            ExitClass();
        }

        public override void VisitEnumDeclaration(EnumDeclarationSyntax node)
        {
            if (node.Modifiers.Any(modifier => modifier.Text == "private"))
            {
                return;
            }

            var cls = new Class(ParseType(node));
            var enumType = new Type("Enum", "enum");
            cls.InheritsFrom.Add(enumType);

            EnterClass(cls);

            _currentNamespace.UsedTypes.Add(enumType);
            CheckForClassSummary(node);

            base.VisitEnumDeclaration(node);

            ExitClass();
        }

        public override void VisitInterfaceDeclaration(InterfaceDeclarationSyntax node)
        {
            if (node.Modifiers.Any(modifier => modifier.Text == "private"))
            {
                return;
            }

            var cls = _currentClass == null
                ? _currentNamespace.GetClassByType(ParseType(node))
                : new Class(ParseType(node));

            EnterClass(cls);

            CheckForClassSummary(node);

            base.VisitInterfaceDeclaration(node);

            ExitClass();
        }

        private void CheckForClassSummary(SyntaxNode node)
        {
            var doc = ParseDocumentation(node);
            if (doc["summary"] != null)
            {
                _currentClass.Summary = GetText(doc["summary"]);
            }
        }

        private Type ParseType(SyntaxNode node)
        {
            return ParseType(_model.GetDeclaredSymbol(node));
        }

        private Type ParseType(ISymbol symbol, string typeName = null)
        {
            var name = typeName ?? symbol.Name;
            var ns = symbol.ContainingNamespace.Name;

            var type = new Type(name, ns != "" ? ns : null);

            if (symbol is INamedTypeSymbol namedSymbol)
            {
                foreach (var typeParameter in namedSymbol.TypeParameters)
                {
                    var parameterName = GetTypeParameterName(typeParameter);

                    if (parameterName != "")
                    {
                        _currentNamespace.TypeParameterNames.Add(parameterName);
                    }

                    type.TypeParameters.Add(ParseType(typeParameter, parameterName));
                }
            }

            return type;
        }

        /// <summary>
        /// In the generated *.pyi files there may be multiple classes in a file.
        /// To prevent against clashing type parameters names this method names them Class_Method_TypeParameterName.
        /// </summary>
        private string GetTypeParameterName(ITypeParameterSymbol symbol)
        {
            var nameParts = new List<string>();

            ISymbol currentType = symbol;
            ISymbol previousCurrentType;

            while (true)
            {
                previousCurrentType = currentType;

                if (previousCurrentType is ITypeParameterSymbol parameterSymbol)
                {
                    currentType = (ISymbol) parameterSymbol.DeclaringMethod ?? parameterSymbol.DeclaringType;
                }

                currentType ??= previousCurrentType.ContainingType;

                if (currentType == null || currentType.Equals(previousCurrentType))
                {
                    break;
                }

                nameParts.Add(previousCurrentType.Name);
            }

            nameParts.Add(previousCurrentType.Name);
            nameParts.Reverse();

            return string.Join("_", nameParts);
        }

        private void EnterClass(Class cls)
        {
            if (_currentClass == null)
            {
                _currentClass = cls;
                _topClass = cls;
            }
            else
            {
                cls.ParentClass = _currentClass;
                _currentClass.InnerClasses.Add(cls);
                _currentClass = cls;
            }
        }

        private void ExitClass()
        {
            _currentClass = _currentClass.ParentClass;

            if (_currentClass == null)
            {
                _topClass = null;
            }
        }

        private XmlElement ParseDocumentation(SyntaxNode node)
        {
            var xmlLines = node
                .GetLeadingTrivia()
                .ToString()
                .Split("\n")
                .Select(line => line.Trim())
                .Select(line =>
                {
                    if (line.StartsWith("/// "))
                    {
                        return line.Substring(4);
                    }

                    if (line.StartsWith("///"))
                    {
                        return line.Substring(3);
                    }

                    return line;
                });

            var xml = string.Join("\n", xmlLines).Replace("&", "&amp;");

            var doc = new XmlDocument();
            doc.LoadXml($"<root>{xml}</root>");

            return doc["root"];
        }

        private string GetText(XmlElement xmlElement)
        {
            var clone = xmlElement.CloneNode(true);

            for (int i = 0, iMax = clone.ChildNodes.Count; i < iMax; i++)
            {
                var child = clone.ChildNodes[i];

                if (child.Name != "see")
                {
                    continue;
                }

                var newNode = clone.OwnerDocument.CreateTextNode(child.Attributes["cref"].InnerText);
                clone.ReplaceChild(newNode, child);
            }

            return clone.InnerText.Trim();
        }
    }
}

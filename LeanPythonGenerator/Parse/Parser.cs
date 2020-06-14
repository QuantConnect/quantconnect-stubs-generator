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
        /// If _currentClass is A.B.C, then _topClass is A.
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
            // Skip private classes
            if (node.Modifiers.Any(modifier => modifier.Text == "private"))
            {
                return;
            }

            var className = node.Identifier.Text;
            var cls = _currentClass == null
                ? _currentNamespace.GetClassByName(className)
                : new Class(className, _currentNamespace);

            EnterClass(cls);

            CheckForClassSummary(node);

            base.VisitClassDeclaration(node);

            ExitClass();
        }

        public override void VisitStructDeclaration(StructDeclarationSyntax node)
        {
            EnterClass(new Class(node.Identifier.Text, _currentNamespace));

            CheckForClassSummary(node);

            base.VisitStructDeclaration(node);

            ExitClass();
        }

        public override void VisitEnumDeclaration(EnumDeclarationSyntax node)
        {
            var cls = new Class(node.Identifier.Text, _currentNamespace);
            var enumType = new Type("Enum", "enum");
            cls.InheritsFrom.Add(enumType);

            EnterClass(cls);

            CheckForClassSummary(node);

            _topClass.RequiredTypes.Add(enumType);

            base.VisitEnumDeclaration(node);

            ExitClass();
        }

        private void CheckForClassSummary(SyntaxNode node)
        {
            var doc = ParseDocumentation(node);
            if (doc["summary"] != null)
            {
                _currentClass.Summary = doc["summary"].InnerText.Trim();
            }
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
    }
}

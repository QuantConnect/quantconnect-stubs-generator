using System.Linq;
using System.Xml;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using QuantConnectStubsGenerator.Model;

namespace QuantConnectStubsGenerator.Parser
{
    public abstract class BaseParser : CSharpSyntaxWalker
    {
        protected readonly ParseContext _context;
        protected readonly SemanticModel _model;

        protected readonly TypeConverter _typeConverter;

        protected Namespace _currentNamespace;
        protected Class _currentClass;

        protected BaseParser(ParseContext context, SemanticModel model)
        {
            _context = context;
            _model = model;

            _typeConverter = new TypeConverter(model);
        }

        public override void VisitNamespaceDeclaration(NamespaceDeclarationSyntax node)
        {
            var name = node.Name.ToString();

            if (!_context.HasNamespace(name))
            {
                _context.RegisterNamespace(new Namespace(name));
            }

            _currentNamespace = _context.GetNamespaceByName(name);
            base.VisitNamespaceDeclaration(node);
            _currentNamespace = null;
        }

        public override void VisitClassDeclaration(ClassDeclarationSyntax node)
        {
            if (HasModifier(node, "private"))
            {
                return;
            }

            EnterClass(node);
            base.VisitClassDeclaration(node);
            ExitClass();
        }

        public override void VisitStructDeclaration(StructDeclarationSyntax node)
        {
            if (HasModifier(node, "private"))
            {
                return;
            }

            EnterClass(node);
            base.VisitStructDeclaration(node);
            ExitClass();
        }

        public override void VisitEnumDeclaration(EnumDeclarationSyntax node)
        {
            if (HasModifier(node, "private"))
            {
                return;
            }

            EnterClass(node);
            base.VisitEnumDeclaration(node);
            ExitClass();
        }

        public override void VisitInterfaceDeclaration(InterfaceDeclarationSyntax node)
        {
            if (HasModifier(node, "private"))
            {
                return;
            }

            EnterClass(node);
            base.VisitInterfaceDeclaration(node);
            ExitClass();
        }

        /// <summary>
        /// EnterClass is the method that is called whenever a class/struct/interface/enum is entered.
        /// In the BaseParser it is assumed that the class that is entered is already registered in the namespace.
        /// In the ClassParser, which runs before any other parsers, this method is overridden to register classes.
        /// </summary>
        protected virtual void EnterClass(BaseTypeDeclarationSyntax node)
        {
            _currentClass = _currentNamespace.GetClassByType(_typeConverter.GetType(node));
        }

        private void ExitClass()
        {
            _currentClass = _currentClass.ParentClass;
        }

        /// <summary>
        /// Check if a node has a modifier like private or static.
        /// </summary>
        protected bool HasModifier(MemberDeclarationSyntax node, string modifier)
        {
            return node.Modifiers.Any(m => m.Text == modifier);
        }

        /// <summary>
        /// Parses the documentation above a node to an XML element.
        /// If the documentation contains a summary, this is then accessible with element["summary"].
        /// </summary>
        protected XmlElement ParseDocumentation(SyntaxNode node)
        {
            var lines = node
                .GetLeadingTrivia()
                .ToString()
                .Trim()
                .Split("\n")
                .Select(line => line.Trim())
                .ToList();

            // LeadingTrivia of a node contains all comments above it
            // We skip everything before the last uncommented line to get only the XML directly above the node
            var skips = 0;
            for (var i = 0; i < lines.Count; i++)
            {
                if (lines[i] == "")
                {
                    skips = i;
                }
            }

            var xmlLines = lines
                .Skip(skips)
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

            if (!xml.StartsWith("<"))
            {
                xml = "";
            }

            var doc = new XmlDocument();
            doc.LoadXml($"<root>{xml}</root>");

            return doc["root"];
        }

        /// <summary>
        /// Prefixes the given summary with the prefix.
        /// An empty line is placed between the prefix and the current summary.
        /// </summary>
        protected string PrefixSummary(string currentSummary, string prefix)
        {
            if (currentSummary == null)
            {
                return prefix;
            }

            return currentSummary.Contains(prefix) ? currentSummary : prefix + "\n\n" + currentSummary;
        }
    }
}

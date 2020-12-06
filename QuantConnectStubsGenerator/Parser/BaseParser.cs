using System.Linq;
using System.Text.RegularExpressions;
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
        }

        public override void VisitClassDeclaration(ClassDeclarationSyntax node)
        {
            if (HasModifier(node, "private") || HasModifier(node, "internal"))
            {
                return;
            }

            EnterClass(node);
            base.VisitClassDeclaration(node);
            ExitClass();
        }

        public override void VisitStructDeclaration(StructDeclarationSyntax node)
        {
            if (HasModifier(node, "private") || HasModifier(node, "internal"))
            {
                return;
            }

            EnterClass(node);
            base.VisitStructDeclaration(node);
            ExitClass();
        }

        public override void VisitEnumDeclaration(EnumDeclarationSyntax node)
        {
            if (HasModifier(node, "private") || HasModifier(node, "internal"))
            {
                return;
            }

            EnterClass(node);
            base.VisitEnumDeclaration(node);
            ExitClass();
        }

        public override void VisitInterfaceDeclaration(InterfaceDeclarationSyntax node)
        {
            if (HasModifier(node, "private") || HasModifier(node, "internal"))
            {
                return;
            }

            EnterClass(node);
            base.VisitInterfaceDeclaration(node);
            ExitClass();
        }

        /// <summary>
        /// EnterClass is the method that is called whenever a class/struct/enum/interface is entered.
        /// In the BaseParser it is assumed that the class that is entered is already registered in the namespace.
        /// In the ClassParser, which runs before any other parsers, this method is overridden to register classes.
        /// </summary>
        protected virtual void EnterClass(BaseTypeDeclarationSyntax node)
        {
            _currentClass = _currentNamespace.GetClassByType(_typeConverter.GetType(node, true));
        }

        private void ExitClass()
        {
            _currentClass = _currentClass?.ParentClass;
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

            try
            {
                doc.LoadXml($"<root>{xml}</root>");
            }
            catch
            {
                doc.LoadXml("<root></root>");
            }

            return doc["root"];
        }

        /// <summary>
        /// Appends the given text to the given summary.
        /// An empty line is placed between the current summary and the given text.
        /// </summary>
        protected string AppendSummary(string currentSummary, string text)
        {
            return currentSummary != null ? currentSummary + "\n\n" + text : text;
        }

        /// <summary>
        /// Format a default C# value into a default Python value.
        /// </summary>
        protected string FormatValue(string value)
        {
            // null to None
            if (value == "null")
            {
                return "None";
            }

            // Boolean true
            if (value == "true")
            {
                return "True";
            }

            // Boolean false
            if (value == "false")
            {
                return "False";
            }

            // Numbers
            if (Regex.IsMatch(value, "^-?[0-9.]+m?$"))
            {
                // If the value is a number, remove a potential suffix like "m" in 1.0m
                if (value.EndsWith("m"))
                {
                    return value.Substring(0, value.Length - 1);
                }

                return value;
            }

            // Strings
            if (Regex.IsMatch(value, "^@?\"[^\"]+\"$"))
            {
                if (value.StartsWith("@"))
                {
                    value = value.Substring(1);
                }

                // Escape backslashes
                value = value.Replace("\\", "\\\\");

                return value;
            }

            return "...";
        }
    }
}

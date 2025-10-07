/*
 * QUANTCONNECT.COM - Democratizing Finance, Empowering Individuals.
 * Lean Algorithmic Trading Engine v2.0. Copyright 2014 QuantConnect Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
*/

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

        /// <summary>
        /// Handles 'namespace QuantConnect.Indicators;' sintax
        /// </summary>
        public override void VisitFileScopedNamespaceDeclaration(FileScopedNamespaceDeclarationSyntax node)
        {
            var name = node.Name.ToString();
            SetCurrentNamespace(name);
            base.VisitFileScopedNamespaceDeclaration(node);
        }

        /// <summary>
        /// Handles 'namespace QuantConnect.Indicators { }' sintax
        /// </summary>
        public override void VisitNamespaceDeclaration(NamespaceDeclarationSyntax node)
        {
            var name = node.Name.ToString();
            SetCurrentNamespace(name);
            base.VisitNamespaceDeclaration(node);
        }

        public override void VisitClassDeclaration(ClassDeclarationSyntax node)
        {
            if (ShouldSkip(node))
            {
                return;
            }

            EnterClass(node);
            base.VisitClassDeclaration(node);
            ExitClass();
        }

        public override void VisitStructDeclaration(StructDeclarationSyntax node)
        {
            if (ShouldSkip(node))
            {
                return;
            }

            EnterClass(node);
            base.VisitStructDeclaration(node);
            ExitClass();
        }

        public override void VisitEnumDeclaration(EnumDeclarationSyntax node)
        {
            if (ShouldSkip(node))
            {
                return;
            }

            EnterClass(node);
            base.VisitEnumDeclaration(node);
            ExitClass();
        }

        public override void VisitInterfaceDeclaration(InterfaceDeclarationSyntax node)
        {
            if (ShouldSkip(node))
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
            _currentClass = _currentNamespace.GetClassByType(_typeConverter.GetType(node, true, true, false));
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
            return HasModifier(node.Modifiers, modifier);
        }

        /// <summary>
        /// Check if a node has a modifier like private or static.
        /// </summary>
        protected bool HasModifier(SyntaxTokenList modifiers, string modifier)
        {
            return modifiers.Any(m => m.Text == modifier);
        }

        /// <summary>
        /// Check if a node has an attribute like Obsolete or StubsIgnore.
        /// </summary>
        protected bool HasAttribute(SyntaxList<AttributeListSyntax> attributeList, string attribute)
        {
            return attributeList.Any(list => list.Attributes.Any(x => x.Name.ToString() == attribute));
        }

        /// <summary>
        /// We skip internal or private nodes
        /// </summary>
        protected bool ShouldSkip(MemberDeclarationSyntax node)
        {
            if (HasAttribute(node.AttributeLists, "StubsIgnore"))
            {
                return true;
            }

            if (HasModifier(node, "private") || HasModifier(node, "internal"))
            {
                return true;
            }

            if (node.Modifiers.Count() == 0 && node.Parent != null && node.Parent.IsKind(SyntaxKind.InterfaceDeclaration))
            {
                // interfaces properties/methods are public by default, so they depend on the parent really
                if (node.Parent is InterfaceDeclarationSyntax interfaceDeclarationSyntax)
                {
                    var modifiers = interfaceDeclarationSyntax.Modifiers;
                    return !HasModifier(modifiers, "public") && !HasModifier(modifiers, "protected");
                }
                return true;
            }
            // some classes don't any access modifier set, which means private
            return !HasModifier(node, "public") && !HasModifier(node, "protected");
        }

        /// <summary>
        /// Returns the deprecation message if the node is marked obsolete, or null if it is not.
        /// </summary>
        protected string GetDeprecationReason(MemberDeclarationSyntax node)
        {
            foreach (var attributeList in node.AttributeLists)
            {
                foreach (var attribute in attributeList.Attributes)
                {
                    if (attribute.Name.ToString() == "Obsolete")
                    {
                        if (attribute.ArgumentList == null)
                        {
                            return "This member is marked as obsolete.";
                        }

                        var arguments = attribute.ArgumentList.Arguments;
                        if (arguments.Count == 0)
                        {
                            return "This member is marked as obsolete.";
                        }

                        var reason = _model.GetConstantValue(arguments[0].Expression);
                        var reasonMessage = reason.HasValue ? reason.Value as string : arguments[0].Expression.ToString();

                        // The stubs are meant to make writing algorithms easier
                        // If a member is not deprecated for algorithm use, we don't mark it as deprecated at all
                        if (!reasonMessage.Contains("provided for algorithm use only"))
                        {
                            return reasonMessage;
                        }
                    }
                }
            }

            return null;
        }

        /// <summary>
        /// Parses the documentation above a node to an XML element.
        /// If the documentation contains a summary, this is then accessible with element["summary"].
        /// </summary>
        protected XmlDocument ParseDocumentation(SyntaxNode node)
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

            var xml = string.Join("\n", xmlLines).Replace("&", "&amp;").Trim();

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

            return doc;
        }

        /// <summary>
        /// Appends the given text to the given summary.
        /// An empty line is placed between the current summary and the given text.
        /// </summary>
        protected string AppendSummary(string currentSummary, string text)
        {
            return currentSummary != null ? currentSummary + "\n\n" + text : text;
        }

        protected XmlDocument GetXmlDocumentation(MemberDeclarationSyntax node, CodeEntityType codeEntityType)
        {
            var doc = ParseDocumentation(node);
            var xmlSummary = doc["root"]["summary"];

            if (HasModifier(node, "protected"))
            {
                var hasSummary = xmlSummary != null;
                xmlSummary ??= doc.CreateElement("summary");
                doc["root"].AppendChild(xmlSummary);
                xmlSummary.AppendChild(doc.CreateTextNode((!hasSummary ? "" : "\n\n") + $"This {nameof(codeEntityType)} is protected."));
            }

            var deprecationReason = GetDeprecationReason(node);
            if (deprecationReason != null)
            {
                var hasSummary = xmlSummary != null;
                xmlSummary ??= doc.CreateElement("summary");
                doc["root"].AppendChild(xmlSummary);
                xmlSummary.AppendChild(doc.CreateTextNode((!hasSummary ? "" : "\n\n") + deprecationReason));
            }

            return doc;
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

        private void SetCurrentNamespace(string name)
        {
            if (!_context.HasNamespace(name))
            {
                _context.RegisterNamespace(new Namespace(name));
            }

            _currentNamespace = _context.GetNamespaceByName(name);
        }
    }
}


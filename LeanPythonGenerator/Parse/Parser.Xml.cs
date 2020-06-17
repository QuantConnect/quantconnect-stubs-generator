using System;
using System.Linq;
using System.Xml;
using Microsoft.CodeAnalysis;

namespace LeanPythonGenerator.Parse
{
    public partial class Parser
    {
        /// <summary>
        /// Parses the documentation above a node to an XML element.
        /// If the documentation contains a summary, this is then accessible with element["summary"].
        /// </summary>
        private XmlElement ParseDocumentation(SyntaxNode node)
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
            catch (Exception)
            {
                doc.LoadXml("<root></root>");
            }

            return doc["root"];
        }
    }
}

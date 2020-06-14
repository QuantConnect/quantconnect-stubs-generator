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

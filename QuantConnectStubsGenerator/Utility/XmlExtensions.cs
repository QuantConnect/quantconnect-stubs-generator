using System.Xml;

namespace QuantConnectStubsGenerator.Utility
{
    public static class XmlExtensions
    {
        public static string GetText(this XmlElement element)
        {
            var clone = element.CloneNode(true);

            for (int i = 0, iMax = clone.ChildNodes.Count; i < iMax; i++)
            {
                var child = clone.ChildNodes[i];

                if (child.Name != "see")
                {
                    continue;
                }

                // Replace cref, paramref and langword tags with their content
                var attribute = child.Attributes["cref"]
                                ?? child.Attributes["paramref"]
                                ?? child.Attributes["langword"];

                var newText = attribute.InnerText;

                // Convert "T:System.Object" to "System.Object"
                if (newText.Length > 2 && newText[1] == ':')
                {
                    newText = newText.Substring(2);
                }

                var newNode = clone.OwnerDocument.CreateTextNode(newText);
                clone.ReplaceChild(newNode, child);
            }

            return clone.InnerText.Trim();
        }
    }
}

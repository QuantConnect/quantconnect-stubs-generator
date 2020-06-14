using System.Xml;

namespace LeanPythonGenerator.Parse
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

                var newNode = clone.OwnerDocument.CreateTextNode(child.Attributes["cref"].InnerText);
                clone.ReplaceChild(newNode, child);
            }

            return clone.InnerText.Trim();
        }
    }
}

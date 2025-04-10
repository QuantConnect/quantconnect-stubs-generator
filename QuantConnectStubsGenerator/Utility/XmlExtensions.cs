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

using System.Net;
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
                string newText = null;

                switch (child.Name)
                {
                    case "typeparamref":
                        newText = child.Attributes["name"].Value;
                        break;
                    case "see":
                    {
                        // Replace cref, paramref, langword and href tags with their content
                        var attribute = child.Attributes["cref"]
                                        ?? child.Attributes["paramref"]
                                        ?? child.Attributes["langword"]
                                        ?? child.Attributes["href"];

                        newText = attribute != null ? attribute.InnerText : child.InnerText;

                        // Convert "T:System.Object" to "System.Object"
                        if (newText.Length > 2 && newText[1] == ':')
                        {
                            newText = newText.Substring(2);
                        }

                        break;
                    }
                }

                if (newText == null)
                {
                    continue;
                }

                var newNode = clone.OwnerDocument.CreateTextNode(newText);
                clone.ReplaceChild(newNode, child);
            }

            var text = clone.InnerText.Trim();

            // Escape backslashes
            text = text.Replace("\\", "\\\\");

            // Decode HTML entities
            text = WebUtility.HtmlDecode(text);

            return text;
        }
    }
}


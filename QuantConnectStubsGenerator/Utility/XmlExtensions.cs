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
using System.Net;
using System.Runtime.CompilerServices;
using System.Xml;
using QuantConnectStubsGenerator.Model;

namespace QuantConnectStubsGenerator.Utility
{
    public static class XmlExtensions
    {
        public static string GetText(this XmlElement element, CodeEntity entity, ParseContext context, bool adjustNames = true)
        {
            var clone = element.CloneNode(true);

            for (int i = 0, iMax = clone.ChildNodes.Count; i < iMax; i++)
            {
                var child = clone.ChildNodes[i];
                string newText = null;

                switch (child.Name)
                {
                    case "paramref":
                    case "typeparamref":
                        newText = adjustNames ? child.Attributes["name"].InnerText.ToSnakeCase() : child.Attributes["name"].InnerText;
                        break;
                    case "see":
                    case "seealso":
                        {
                            // Replace cref, paramref, langword and href tags with their content
                            var attribute = child.Attributes["langword"] ?? child.Attributes["href"];
                            if (attribute != null)
                            {
                                newText = attribute.InnerText;
                            }
                            else if ((attribute = child.Attributes["paramref"]) != null)
                            {
                                newText = adjustNames ? attribute.InnerText.ToSnakeCase() : attribute.InnerText;
                            }
                            else if ((attribute = child.Attributes["cref"]) != null)
                            {
                                newText = attribute.InnerText;

                                if (adjustNames)
                                {
                                    var parts = newText.Split('.');
                                    var name = parts[^1];
                                    var parenthesisIndex = parts[^1].IndexOf('(');
                                    var isMethod = false;
                                    if (parenthesisIndex != -1)
                                    {
                                        parts[^1] = name = name.Substring(0, parenthesisIndex);
                                        isMethod = true;
                                    }

                                    var referencedEntity = GetCodeEntity(name, newText, parts, entity, context, isMethod);
                                    if (referencedEntity != null)
                                    {
                                        if (referencedEntity is Method)
                                        {
                                            newText = newText.Replace(name, name.ToSnakeCase());
                                        }
                                        else if (referencedEntity is Property property)
                                        {
                                            newText = newText.Replace(name, name.ToSnakeCase(constant: property.Constant));
                                        }
                                    }
                                    // else: null or a class, assume it's a class, no need to change anything
                                }
                            }
                            else
                            {
                                newText = child.InnerText;
                            }

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

        /// <summary>
        /// This will try to find the referenced entity (class, method or property/field) in the XML documentation.
        /// It will first look in the current class, then in the imported namespaces.
        /// </summary>
        private static CodeEntity GetCodeEntity(string name, string fullName, string[] parts, CodeEntity entity, ParseContext context, bool isMethod)
        {
            if (string.IsNullOrEmpty(name) || context == null)
            {
                return null;
            }

            var entityClass = entity switch
            {
                Class c => c,
                Property p => p.Class,
                Method m => m.Class,
            };

            if (parts.Length == 1)
            {
                // Could be either a method or a property of the class itself
                var method = entityClass.Methods.FirstOrDefault(x => x.Name == parts[0]);
                if (method != null)
                {
                    return method;
                }

                var property = entityClass.Properties.FirstOrDefault(x => x.Name == parts[0]);
                if (property != null)
                {
                    return property;
                }

                // It's  a class, let's try to find it
                var ns = context.GetNamespaceByName(entityClass.Type.Namespace);
                return context.GetNamespaces()
                    .Where(x => x.Name.StartsWith("QuantConnect") && IsInNamespace(x, ns))
                    .SelectMany(x => x.GetClasses())
                    .FirstOrDefault(x => x.Type.Name == fullName);
            }

            var entityNamespace = context.GetNamespaceByName(entityClass.Type.Namespace);

            foreach (var ns in context.GetNamespaces().Where(x => x.Name.StartsWith("QuantConnect")))
            {
                foreach (var cls in ns.GetClasses())
                {
                    foreach (var method in cls.Methods)
                    {
                        if (method.Name == name && BelongsToClass(fullName, cls) && IsInNamespace(ns, entityNamespace))
                        {
                            return method;
                        }
                    }

                    // Not a method
                    if (!isMethod)
                    {
                        // Could be a property of the current class
                        foreach (var property in cls.Properties)
                        {
                            if (property.Name == name && BelongsToClass(fullName, cls) && IsInNamespace(ns, entityNamespace))
                            {
                                return property;
                            }
                        }

                        // Not a property, could be the current class itself
                        if (cls.Type.Name == fullName && IsInNamespace(ns, entityNamespace))
                        {
                            return cls;
                        }
                    }
                }
            }

            return null;
        }

        [MethodImpl(MethodImplOptions.AggressiveInlining)]
        private static bool BelongsToClass(string fullName, Class cls)
        {
            return fullName.Substring(0, fullName.LastIndexOf('.')) == cls.Type.Name;
        }

        [MethodImpl(MethodImplOptions.AggressiveInlining)]
        private static bool IsInNamespace(Namespace ns, Namespace entityNamespace)
        {
            return ns.Name == entityNamespace.Name || entityNamespace.NamespacesToImport.Contains(ns.Name);
        }
    }
}


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

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using QuantConnectStubsGenerator.Model;
using QuantConnectStubsGenerator.Utility;

namespace QuantConnectStubsGenerator.Renderer
{
    public class PropertyRenderer : ObjectRenderer<Property>
    {
        public PropertyRenderer(TextWriter writer, int indentationLevel, ParseContext context)
            : base(writer, indentationLevel, context)
        {
        }

        public override void Render(Property property)
        {
            var snakeCasedProperty = GetSnakeCasedProperty(property);
            if (snakeCasedProperty != null)
            {
                property = snakeCasedProperty;
            }

            if (ShouldSkip(property))
            {
                return;
            }

            if (property.Static)
            {
                RenderAttribute(property);
            }
            else
            {
                RenderProperty(property);
            }
        }

        private bool TryGetClass(PythonType classType, string namespaceName, out Class @class)
        {
            @class = null;
            if (namespaceName == null || classType == null)
            {
                return false;
            }

            try
            {
                var @namespace = Context.GetNamespaceByName(namespaceName);
                @class = @namespace.GetClassByType(classType);
                return true;
            }
            catch (ArgumentException)
            {
                // Class not found:
                //   - The type was converted to a Python type (e.g. DateTime -> datetime),
                //     so the class will not be found in any namespace, no need to check. Or,
                //   - The class is private or internal, it won't be found in the namespaces.
                return false;
            }
        }

        private bool ShouldSkip(Property property)
        {
            // Python.Net will favor snake-cased methods over properties,
            // so we skip properties what match an existing method's name

            var checkedClasses = new HashSet<PythonType>();
            var classes = new Queue<Class>();
            classes.Enqueue(property.Class);
            while (classes.TryDequeue(out var @class))
            {
                if (@class.Methods.Any(method => method.Name == property.Name))
                {
                    return true;
                }

                checkedClasses.Add(@class.Type);

                // Now we need to do the same check of the inherited classes
                foreach (var inheritedClassType in @class.InheritsFrom)
                {
                    if (checkedClasses.Contains(inheritedClassType))
                    {
                        continue;
                    }

                    if (TryGetClass(inheritedClassType, inheritedClassType.Namespace, out var inheritedClass))
                    {
                        classes.Enqueue(inheritedClass);
                    }
                    else
                    {
                        checkedClasses.Add(inheritedClassType);
                    }
                }
            }

            return false;
        }

        private static Property GetSnakeCasedProperty(Property property)
        {
            var name = property.Name.ToSnakeCase(property.Constant);
            if (name.IsPythonReservedWord())
            {
                return null;
            }

            return new Property(property, name);
        }

        private void RenderAttribute(Property property)
        {
            // Some attributes have names in C# that are illegal in Python
            if (property.Name == "None" || property.Name == "True" || property.Name == "False")
            {
                Write("# Cannot convert to Python: ");
            }

            Write(property.Name);

            if (property.Type != null)
            {
                Write($": {property.Type.ToPythonString()}");
            }

            if (property.Value != null)
            {
                Write($" = {property.Value}");
            }

            WriteLine();

            WriteSummary(property.Summary);
            WriteLine();
        }

        private void RenderProperty(Property property)
        {
            // Some properties have names starting with "@", which is invalid in Python
            if (property.Name.StartsWith("@"))
            {
                WriteLine($"# Cannot convert property {property.Name} to Python");
                WriteLine();
                return;
            }

            WriteLine("@property");

            if (property.Abstract)
            {
                WriteLine("@abc.abstractmethod");
            }

            // Add the getter
            WriteLine($"def {property.Name}(self) -> {property.Type.ToPythonString()}:");
            WriteSummary(property.Summary, true);

            if (property.DeprecationReason != null)
            {
                WriteLine($"warnings.warn(\"{property.DeprecationReason}\", DeprecationWarning)".Indent());
            }
            else
            {
                WriteLine("...".Indent());
            }

            WriteLine();

            // render setter for mypy to be happy
            if (property.HasSetter)
            {
                WriteLine("@property.setter");

                // Add the getter
                WriteLine($"def {property.Name}(self, value: {property.Type.ToPythonString()}) -> None:");
                if (property.DeprecationReason != null)
                {
                    WriteLine($"warnings.warn(\"{property.DeprecationReason}\", DeprecationWarning)".Indent());
                }
                else
                {
                    WriteLine("...".Indent());
                }

                WriteLine();
            }
        }
    }
}


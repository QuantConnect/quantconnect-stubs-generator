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

namespace QuantConnectStubsGenerator.Renderer
{
    public class ClassRenderer : ObjectRenderer<Class>
    {
        public ClassRenderer(TextWriter writer, int indentationLevel, ParseContext context)
            : base(writer, indentationLevel, context)
        {
        }

        public override void Render(Class cls)
        {
            RenderClassHeader(cls);
            RenderInnerClasses(cls);
            RenderProperties(cls);
            RenderMethods(cls);
        }

        private void RenderClassHeader(Class cls)
        {
            Write($"class {cls.Type.Name.Split(".").Last()}");

            var inherited = new List<string>();

            if (cls.Type.TypeParameters.Count > 0)
            {
                var types = cls.Type.TypeParameters.Select(type => type.ToPythonString());
                inherited.Add($"typing.Generic[{string.Join(", ", types)}]");
            }

            foreach (var inheritedType in cls.InheritsFrom)
            {
                inherited.Add(inheritedType.ToPythonString());
            }

            if (cls.MetaClass != null)
            {
                inherited.Add($"metaclass={cls.MetaClass.ToPythonString()}");
            }

            if (inherited.Count > 0)
            {
                for (var i = 0; i < inherited.Count; i++)
                {
                    if (inherited[i].Equals("System.Enum", StringComparison.InvariantCultureIgnoreCase))
                    {
                        // 'Enum' is a python base type which is handled better by mypy if we used 'System' it assumes the enum value and causes a warning/missmatch
                        inherited[i] = "Enum";
                    }
                }
                Write($"({string.Join(", ", inherited)})");
            }

            WriteLine(":");

            WriteSummary(cls.Summary ?? "This class has no documentation.", true);
            WriteLine();
        }

        private void RenderInnerClasses(Class cls)
        {
            var classRenderer = CreateRenderer<ClassRenderer>();

            foreach (var innerClass in cls.InnerClasses)
            {
                classRenderer.Render(innerClass);
            }
        }

        private void RenderProperties(Class cls)
        {
            var propertyRenderer = CreateRenderer<PropertyRenderer>();

            foreach (var property in cls.Properties)
            {
                propertyRenderer.Render(property);
            }
        }

        private void RenderMethods(Class cls)
        {
            var methodRenderer = CreateRenderer<MethodRenderer>();

            // Some methods have two variants where one is deprecated
            // PyCharm complains if you override the second/third/fourth/etc. overload of a method
            // We therefore need to render deprecated methods after non-deprecated ones
            // This way PyCharm doesn't complain if you override the non-deprecated method
            var orderedMethods = cls.Methods
                .Where(m => !string.IsNullOrEmpty(m.Name))
                .OrderBy(m => m.Name)
                .ThenBy(m => m.DeprecationReason == null ? 0 : 1);

            foreach (var method in orderedMethods)
            {
                methodRenderer.Render(method);
            }
        }
    }
}


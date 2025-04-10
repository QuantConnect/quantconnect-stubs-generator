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
    public class NamespaceRenderer : ObjectRenderer<Namespace>
    {
        public NamespaceRenderer(TextWriter writer, int indentationLevel, ParseContext context)
            : base(writer, indentationLevel, context)
        {
        }

        public override void Render(Namespace ns)
        {
            // Fix for Jedi; Include import of typing instead of using typing.overload
            WriteLine("from typing import overload");
            // fix for python enums
            WriteLine("from enum import Enum");

            var usedTypes = ns
                .GetParentClasses()
                .SelectMany(cls => cls.GetUsedTypes())
                .ToList();

            RenderImports(usedTypes);
            RenderTypeAliases(usedTypes);
            RenderTypeVars(usedTypes);

            WriteLine();

            RenderClasses(ns);
        }

        private void RenderImports(IEnumerable<PythonType> usedTypes)
        {
            // Retrieve all used namespaces
            var namespacesToImport = usedTypes
                .Where(type => type.Namespace != null)
                .Select(type => type.Namespace)
                .Distinct()
                .OrderBy(namespaceToImport => namespaceToImport, StringComparer.Ordinal)
                .ToList();

            if (namespacesToImport.Count == 0)
            {
                return;
            }

            var systemNamespaces = namespacesToImport.Where(ns => char.IsLower(ns[0]) && ns != "pandas").ToList();
            var nonSystemNamespaces = namespacesToImport.Except(systemNamespaces).ToList();

            foreach (var ns in systemNamespaces)
            {
                WriteLine($"import {ns}");
            }

            if (systemNamespaces.Count > 0 && nonSystemNamespaces.Count > 0)
            {
                WriteLine();
            }

            foreach (var ns in nonSystemNamespaces)
            {
                WriteLine($"import {ns}");
            }

            WriteLine();
        }

        private void RenderTypeAliases(IEnumerable<PythonType> usedTypes)
        {
            var typeAliases = usedTypes
                .Where(type => type.Alias != null)
                .GroupBy(type => type.Alias)
                .Select(group => group.First())
                .ToList();

            if (typeAliases.Count == 0)
            {
                return;
            }

            foreach (var type in typeAliases)
            {
                WriteLine($"{type.Alias} = {type.ToPythonString(true)}");
            }

            WriteLine();
        }

        private void RenderTypeVars(IEnumerable<PythonType> usedTypes)
        {
            var typeVars = usedTypes
                .Where(type => type.IsNamedTypeParameter)
                .Select(type => type.ToPythonString())
                .Distinct()
                .ToList();

            if (typeVars.Count == 0)
            {
                return;
            }

            foreach (var name in typeVars)
            {
                WriteLine($"{name} = typing.TypeVar(\"{name}\")");
            }

            WriteLine();
        }

        private void RenderClasses(Namespace ns)
        {
            var dependencyGraph = new DependencyGraph();

            foreach (var cls in ns.GetParentClasses())
            {
                dependencyGraph.AddClass(cls);
            }

            foreach (var cls in ns.GetParentClasses())
            {
                foreach (var type in cls.GetUsedTypes())
                {
                    dependencyGraph.AddDependency(cls, type);
                }
            }

            var classRenderer = CreateRenderer<ClassRenderer>(false);

            foreach (var cls in dependencyGraph.GetClassesInOrder())
            {
                classRenderer.Render(cls);
                WriteLine();
            }
        }
    }
}


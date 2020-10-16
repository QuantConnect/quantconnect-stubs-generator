using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using QuantConnectStubsGenerator.Model;
using QuantConnectStubsGenerator.Utility;

namespace QuantConnectStubsGenerator.Renderer
{
    public class NamespaceRenderer : BaseRenderer<Namespace>
    {
        private IList<PythonType> _usedTypes;

        public NamespaceRenderer(StreamWriter writer, int indentationLevel, Namespace ns)
            : base(writer, indentationLevel, ns)
        {
        }

        public override void Render(Namespace ns)
        {
            _usedTypes = ns
                .GetParentClasses()
                .SelectMany(cls => cls.GetUsedTypes())
                .ToList();

            RenderImports(ns);
            RenderTypeAliases(ns);
            RenderTypeVars(ns);
            RenderClasses(ns);
        }

        private void RenderImports(Namespace ns)
        {
            // Retrieve all used namespaces
            var namespacesToImport = _usedTypes
                .Where(type => type.Namespace != null)
                .Select(type => type.Namespace)
                .Where(nsStr => nsStr != ns.Name)
                .Distinct()
                .OrderBy(namespaceToImport => namespaceToImport, StringComparer.Ordinal)
                .ToList();

            if (namespacesToImport.Count == 0)
            {
                return;
            }

            foreach (var namespaceToImport in namespacesToImport)
            {
                WriteLine($"import {namespaceToImport}");
            }

            WriteLine();
            WriteLine();
        }

        private void RenderTypeAliases(Namespace ns)
        {
            var typeAliases = _usedTypes
                .Where(type => type.Alias != null)
                .Where(type => type.Namespace != ns.Name)
                .GroupBy(type => type.Alias)
                .Select(group => group.First())
                .ToList();

            if (typeAliases.Count == 0)
            {
                return;
            }

            foreach (var type in typeAliases)
            {
                WriteLine($"{type.Alias} = {type.ToPythonString(ns, true)}");
            }

            WriteLine();
            WriteLine();
        }

        private void RenderTypeVars(Namespace ns)
        {
            var typeVars = _usedTypes
                .Where(type => type.IsNamedTypeParameter)
                .Select(type => type.ToPythonString(ns))
                .Distinct()
                .ToList();

            if (typeVars.Count == 0)
            {
                return;
            }

            foreach (var name in typeVars)
            {
                WriteLine($"{name} = typing.TypeVar('{name}')");
            }

            WriteLine();
            WriteLine();
        }

        private void RenderClasses(Namespace ns)
        {
            var typeAliasesByBaseName = _usedTypes
                .Where(type => type.Alias != null)
                .Where(type => type.Namespace == ns.Name)
                .ToLookup(type => type.GetBaseName());

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

                if (!typeAliasesByBaseName.Contains(cls.Type.Name))
                {
                    continue;
                }

                var aliases = typeAliasesByBaseName[cls.Type.Name]
                    .GroupBy(type => type.Alias)
                    .Select(group => group.First());

                foreach (var type in aliases)
                {
                    WriteLine($"{type.Alias} = {type.ToPythonString(ns, true)}");
                }

                WriteLine();
                WriteLine();
            }
        }
    }
}

using System;
using System.IO;
using System.Linq;
using LeanPythonGenerator.Model;

namespace LeanPythonGenerator.Render
{
    public class NamespaceRenderer : BaseRenderer<Namespace>
    {
        public NamespaceRenderer(StreamWriter writer, int indentationLevel) : base(writer, indentationLevel)
        {
        }

        public override void Render(Namespace ns)
        {
            RenderImports(ns);
            RenderTypeAliases(ns);
            RenderTypeVars(ns);
            RenderClasses(ns);
        }

        private void RenderImports(Namespace ns)
        {
            // Retrieve all used types from all top-level classes
            var typesToImport = ns
                .GetClasses()
                .SelectMany(cls => cls.UsedTypes)
                .Where(type => type.Namespace != null && type.Namespace != ns.Name)
                .OrderBy(type => type.Namespace, StringComparer.Ordinal)
                .GroupBy(type => type.Namespace)
                .ToList();

            if (typesToImport.Count == 0)
            {
                return;
            }

            foreach (var group in typesToImport)
            {
                var types = group
                    .Select(type => type.Name.Split(".")[0])
                    .Distinct();

                WriteLine($"from {group.Key} import {string.Join(", ", types)}");
            }

            WriteLine();
            WriteLine();
        }

        private void RenderTypeAliases(Namespace ns)
        {
            if (ns.TypeAliases.Count == 0)
            {
                return;
            }

            foreach (var alias in ns.TypeAliases)
            {
                WriteLine($"{alias.Alias} = {alias.ActualType.ToString(ns, true)}");
            }

            WriteLine();
            WriteLine();
        }

        private void RenderTypeVars(Namespace ns)
        {
            var typeVarNames = ns
                .TypeParameterNames
                .OrderBy(name => name)
                .ToList();

            if (typeVarNames.Count == 0)
            {
                return;
            }

            foreach (var name in typeVarNames)
            {
                WriteLine($"{name} = TypeVar('{name}')");
            }

            WriteLine();
            WriteLine();
        }

        /// <summary>
        /// Renders all classes in such an order that the least amount of forward references are needed.
        /// </summary>
        private void RenderClasses(Namespace ns)
        {
            var classRenderer = new ClassRenderer(_writer, _indentationLevel, ns);

            var classesToRender = ns.GetClasses().ToList();

            // Prepare each class' UsedTypes set
            foreach (var cls in classesToRender)
            {
                cls.UsedTypes = cls.UsedTypes.Where(type => type.Namespace == ns.Name).ToHashSet();
            }

            while (classesToRender.Count > 0)
            {
                // Sort the classes based on the amount of forward referenced types
                classesToRender = classesToRender.OrderBy(cls => cls.UsedTypes.Count).ToList();

                var classToRender = classesToRender[0];
                classesToRender.RemoveAt(0);

                classRenderer.Render(classToRender);

                ns.DefinedInternalTypes.Add(classToRender.Type);

                // Remove the rendered class from all other class' UsedTypes sets
                foreach (var cls in classesToRender)
                {
                    cls.UsedTypes = cls.UsedTypes.Where(type => !type.Equals(classToRender.Type)).ToHashSet();
                }
            }
        }
    }
}

using System.IO;
using System.Linq;
using LeanPythonGenerator.Model;

namespace LeanPythonGenerator.Render
{
    public class NamespaceRenderer : BaseRenderer<Namespace>
    {
        private readonly ClassRenderer _classRenderer;

        public NamespaceRenderer(StreamWriter writer, int indentationLevel) : base(writer, indentationLevel)
        {
            _classRenderer = new ClassRenderer(writer, indentationLevel);
        }

        public override void Render(Namespace ns)
        {
            RenderImports(ns);
            RenderClasses(ns);
        }

        private void RenderImports(Namespace ns)
        {
            // Retrieve all required types from all top-level classes
            var typesToImport = ns
                .GetClasses()
                .SelectMany(cls => cls.RequiredTypes)
                .Where(type => type.Namespace != ns.Name)
                .OrderBy(type => type.Namespace)
                .GroupBy(type => type.Namespace)
                .ToList();

            if (typesToImport.Count == 0)
            {
                return;
            }

            foreach (var group in typesToImport)
            {
                var types = group
                    .Select(type => type.Name)
                    .Distinct()
                    .OrderBy(name => name);

                WriteLine($"from {group.Key} import {string.Join(", ", types)}");
            }

            WriteLine();
        }

        private void RenderClasses(Namespace ns)
        {
            var classes = ns.GetClasses().ToList();
            for (int i = 0, iMax = classes.Count; i < iMax; i++)
            {
                _classRenderer.Render(classes[i]);

                if (i != iMax - 1)
                {
                    WriteLine();
                }
            }
        }
    }
}

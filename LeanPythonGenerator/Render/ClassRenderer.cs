using System.Collections.Generic;
using System.IO;
using System.Linq;
using LeanPythonGenerator.Model;
using LeanPythonGenerator.Utility;

namespace LeanPythonGenerator.Render
{
    public class ClassRenderer : BaseRenderer<Class>
    {
        public ClassRenderer(StreamWriter writer, int indentationLevel) : base(writer, indentationLevel)
        {
        }

        public override void Render(Class cls)
        {
            RenderClassHeader(cls);
            RenderInnerClasses(cls);
            RenderProperties(cls);
        }

        private void RenderClassHeader(Class cls)
        {
            Write($"class {cls.Type.Name.Split(".").Last()}");

            var inherited = new List<string>();

            var typeParameters = cls.Type.TypeParameters;
            if (typeParameters.Count > 0)
            {
                var types = typeParameters.Select(type => type.ToString());
                inherited.Add($"Generic[{string.Join(", ", types)}]");
            }

            if (cls.InheritsFrom.Count > 0)
            {
                foreach (var inheritedType in cls.InheritsFrom)
                {
                    inherited.Add(inheritedType.ToString(cls.Type.Namespace));
                }
            }

            if (inherited.Count > 0)
            {
                Write($"({string.Join(", ", inherited)})");
            }

            WriteLine(":");

            if (cls.Summary != null)
            {
                WriteLine($"\"\"\"\n{cls.Summary}\n\"\"\"".Indent());
                WriteLine();
            }
        }

        private void RenderInnerClasses(Class cls)
        {
            var innerRenderer = new ClassRenderer(_writer, _indentationLevel + 1);

            foreach (var innerCls in cls.InnerClasses)
            {
                innerRenderer.Render(innerCls);
                WriteLine();
            }
        }

        private void RenderProperties(Class cls)
        {
            var propertyRenderer = new PropertyRenderer(_writer, _indentationLevel + 1, cls);

            foreach (var property in cls.Properties)
            {
                propertyRenderer.Render(property);
                WriteLine();
            }
        }
    }
}

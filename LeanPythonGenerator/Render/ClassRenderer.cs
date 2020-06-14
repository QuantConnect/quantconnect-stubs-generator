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
            Write($"class {cls.Type.Name}");

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
                WriteLine($"'''\n{cls.Summary}\n'''".Indent());
                WriteLine();
            }

            foreach (var innerCls in cls.InnerClasses)
            {
                var renderer = new ClassRenderer(_writer, _indentationLevel + 1);
                renderer.Render(innerCls);
                WriteLine();
            }
        }
    }
}

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
            Write($"class {cls.Name}");

            if (cls.InheritsFrom.Count > 0)
            {
                var types = cls.InheritsFrom.Select(type => GetTypeName(cls, type));
                Write($"({string.Join(", ", types)})");
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

        private string GetTypeName(Class cls, Type type)
        {
            // Quote all non-imported types because there may be forward references
            return type.Namespace == cls.Namespace.Name ? $"'{type.Name}'" : type.Name;
        }
    }
}

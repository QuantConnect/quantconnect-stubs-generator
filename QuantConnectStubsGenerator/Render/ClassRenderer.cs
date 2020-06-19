using System.Collections.Generic;
using System.IO;
using System.Linq;
using QuantConnectStubsGenerator.Utility;
using QuantConnectStubsGenerator.Model;

namespace QuantConnectStubsGenerator.Render
{
    public class ClassRenderer : BaseRenderer<Class>
    {
        private readonly Namespace _namespace;

        public ClassRenderer(StreamWriter writer, int indentationLevel, Namespace ns) : base(writer, indentationLevel)
        {
            _namespace = ns;
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
                    inherited.Add(inheritedType.ToString(_namespace));
                }
            }

            if (inherited.Count > 0)
            {
                Write($"({string.Join(", ", inherited)})");
            }

            WriteLine(":");
            WriteLine($"\"\"\"\n{cls.Summary ?? "This class has no documentation."}\n\"\"\"".Indent());
            WriteLine();
            WriteLine();
        }

        private void RenderInnerClasses(Class cls)
        {
            var innerRenderer = new ClassRenderer(_writer, _indentationLevel + 1, _namespace);

            foreach (var innerCls in cls.InnerClasses)
            {
                innerRenderer.Render(innerCls);
            }
        }

        private void RenderProperties(Class cls)
        {
            var propertyRenderer = new PropertyRenderer(_writer, _indentationLevel + 1, _namespace);

            foreach (var property in cls.Properties)
            {
                propertyRenderer.Render(property);
            }
        }

        private void RenderMethods(Class cls)
        {
            var methodRenderer = new MethodRenderer(_writer, _indentationLevel + 1, _namespace);

            foreach (var method in cls.Methods)
            {
                methodRenderer.Render(method);
            }
        }
    }
}

using System.Collections.Generic;
using System.IO;
using System.Linq;
using QuantConnectStubsGenerator.Model;

namespace QuantConnectStubsGenerator.Renderer
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

            foreach (var method in cls.Methods)
            {
                methodRenderer.Render(method);
            }
        }
    }
}

using System.Collections.Generic;
using System.IO;
using System.Linq;
using QuantConnectStubsGenerator.Model;

namespace QuantConnectStubsGenerator.Renderer
{
    public class ClassRenderer : ObjectRenderer<Class>
    {
        public ClassRenderer(StreamWriter writer, int indentationLevel) : base(writer, indentationLevel)
        {
        }

        public override void Render(Class cls)
        {
            // Enums are no longer modeled as classes but as constants in their own module for better auto completion
            if (cls.IsEnum())
            {
                RenderEnum(cls);
                return;
            }

            RenderClassHeader(cls);
            RenderEnumsImports(cls);
            RenderInnerClasses(cls);
            RenderProperties(cls);
            RenderMethods(cls);
        }

        private void RenderEnum(Class cls)
        {
            WriteSummary(cls.Summary ?? "This enum has no documentation.", false);
            WriteLine();

            RenderProperties(cls);
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

        private void RenderEnumsImports(Class cls)
        {
            var enumRenderer = CreateRenderer<EnumImportRenderer>();
            var enumsRendered = false;
            foreach (var enumClass in cls.InnerClasses.Where(x => x.IsEnum()))
            {
                enumRenderer.Render(enumClass);
                enumsRendered = true;
            }

            if (enumsRendered)
            {
                WriteLine();
            }
        }

        private void RenderInnerClasses(Class cls)
        {
            var classRenderer = CreateRenderer<ClassRenderer>();

            foreach (var innerClass in cls.InnerClasses.Where(x => !x.IsEnum()))
            {
                classRenderer.Render(innerClass);
            }
        }

        private void RenderProperties(Class cls)
        {
            var propertyRenderer = CreateRenderer<PropertyRenderer>(!cls.IsEnum());

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

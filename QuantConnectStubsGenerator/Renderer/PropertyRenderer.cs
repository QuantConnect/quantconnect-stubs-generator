using System.IO;
using QuantConnectStubsGenerator.Model;
using QuantConnectStubsGenerator.Utility;

namespace QuantConnectStubsGenerator.Renderer
{
    public class PropertyRenderer : BaseRenderer<Property>
    {
        public PropertyRenderer(StreamWriter writer, int indentationLevel, Namespace ns)
            : base(writer, indentationLevel, ns)
        {
        }

        public override void Render(Property property)
        {
            if (property.Static)
            {
                RenderAttribute(property);
            }
            else
            {
                RenderProperty(property);
            }
        }

        private void RenderAttribute(Property property)
        {
            // Some attributes are named "None" in C#, which is a keyword in Python
            if (property.Name == "None")
            {
                Write("# Cannot convert to Python: ");
            }

            Write(property.Name);

            if (property.Type != null)
            {
                Write($": {property.Type.ToPythonString(CurrentNamespace)}");
            }

            if (property.Value != null)
            {
                Write($" = {property.Value}");
            }

            WriteLine();

            if (property.Summary != null)
            {
                WriteLine($"\"\"\"\n{property.Summary}\n\"\"\"");
            }

            WriteLine();
            WriteLine();
        }

        private void RenderProperty(Property property)
        {
            // Some properties have names starting with "@", which is invalid in Python
            if (property.Name.StartsWith("@"))
            {
                WriteLine($"# Cannot convert property {property.Name} to Python");
                WriteLine();
                WriteLine();
                return;
            }

            WriteLine("@property");

            // Mypy has an issue which makes it impossible to use @property and @*.setter along with another decorator
            // See https://github.com/python/mypy/issues/1362
            // Re-enable this when the issue linked above is fixed
            if (property.Abstract)
            {
                // WriteLine("@abc.abstractmethod");
            }

            // Add the getter
            WriteLine($"def {property.Name}(self) -> {property.Type.ToPythonString(CurrentNamespace)}:");

            if (property.Summary != null)
            {
                WriteLine($"\"\"\"\n{property.Summary}\n\"\"\"".Indent());
            }

            WriteLine("...".Indent());
            WriteLine();
            WriteLine();

            if (property.ReadOnly)
            {
                return;
            }

            WriteLine($"@{property.Name}.setter");

            // Mypy has an issue which makes it impossible to use @property and @*.setter along with another decorator
            // See https://github.com/python/mypy/issues/1362
            // Re-enable this when the issue linked above is fixed
            if (property.Abstract)
            {
                // WriteLine("@abc.abstractmethod");
            }

            // Add the setter
            WriteLine($"def {property.Name}(self, value: {property.Type.ToPythonString(CurrentNamespace)}):");

            if (property.Summary != null)
            {
                WriteLine($"\"\"\"\n{property.Summary}\n\"\"\"".Indent());
            }

            WriteLine("...".Indent());
            WriteLine();
            WriteLine();
        }
    }
}

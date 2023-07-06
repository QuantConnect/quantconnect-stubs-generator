using System.IO;
using QuantConnectStubsGenerator.Model;
using QuantConnectStubsGenerator.Utility;

namespace QuantConnectStubsGenerator.Renderer
{
    public class PropertyRenderer : ObjectRenderer<Property>
    {
        public PropertyRenderer(StreamWriter writer, int indentationLevel) : base(writer, indentationLevel)
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
            // Some attributes have names in C# that are illegal in Python
            if (property.Name == "None" || property.Name == "True" || property.Name == "False")
            {
                Write("# Cannot convert to Python: ");
            }

            Write(property.Name);

            if (property.Type != null)
            {
                Write($": {property.Type.ToPythonString()}");
            }

            if (property.Value != null)
            {
                Write($" = {property.Value}");
            }

            WriteLine();

            WriteSummary(property.Summary);
            WriteLine();
        }

        private void RenderProperty(Property property)
        {
            // Some properties have names starting with "@", which is invalid in Python
            if (property.Name.StartsWith("@"))
            {
                WriteLine($"# Cannot convert property {property.Name} to Python");
                WriteLine();
                return;
            }

            WriteLine("@property");

            if (property.Abstract)
            {
                WriteLine("@abc.abstractmethod");
            }

            // Add the getter
            WriteLine($"def {property.Name}(self) -> {property.Type.ToPythonString()}:");
            WriteSummary(property.Summary, true);

            if (property.DeprecationReason != null)
            {
                WriteLine($"warnings.warn(\"{property.DeprecationReason}\", DeprecationWarning)".Indent());
            }
            else
            {
                WriteLine("...".Indent());
            }

            WriteLine();
        }
    }
}

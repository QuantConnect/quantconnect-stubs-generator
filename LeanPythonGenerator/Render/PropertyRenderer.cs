using System.IO;
using LeanPythonGenerator.Model;
using LeanPythonGenerator.Utility;

namespace LeanPythonGenerator.Render
{
    public class PropertyRenderer : BaseRenderer<Property>
    {
        private readonly Class _class;

        public PropertyRenderer(StreamWriter writer, int indentationLevel, Class cls) : base(writer, indentationLevel)
        {
            _class = cls;
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
            if (property.Summary != null)
            {
                WriteLine($"\"\"\"\n{property.Summary}\n\"\"\"");
            }

            Write(property.Name);

            if (property.Type != null)
            {
                Write($": {property.Type.ToString(_class.Type.Namespace)}");
            }

            if (property.Value != null)
            {
                Write($" = {property.Value}");
            }

            WriteLine();
            WriteLine();
            WriteLine();
        }

        private void RenderProperty(Property property)
        {
            WriteLine("@property");

            if (property.Abstract)
            {
                WriteLine("@abstractmethod");
            }

            WriteLine($"def {property.Name}(self) -> {property.Type.ToString(_class.Type.Namespace)}:");

            if (property.Summary != null)
            {
                WriteLine($"\"\"\"\n{property.Summary}\n\"\"\"".Indent());
            }

            WriteLine("pass".Indent());
            WriteLine();
            WriteLine();

            if (property.ReadOnly)
            {
                return;
            }

            WriteLine($"@{property.Name}.setter");

            if (property.Abstract)
            {
                WriteLine("@abstractmethod");
            }

            WriteLine($"def {property.Name}(self, value: {property.Type.ToString(_class.Type.Namespace)}):");

            if (property.Summary != null)
            {
                WriteLine($"\"\"\"\n{property.Summary}\n\"\"\"".Indent());
            }

            WriteLine("pass".Indent());
            WriteLine();
            WriteLine();
        }
    }
}

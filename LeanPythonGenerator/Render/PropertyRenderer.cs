using System.IO;
using LeanPythonGenerator.Model;
using LeanPythonGenerator.Utility;

namespace LeanPythonGenerator.Render
{
    public class PropertyRenderer : BaseRenderer<Property>
    {
        private readonly Namespace _namespace;

        public PropertyRenderer(StreamWriter writer, int indentationLevel, Namespace ns)
            : base(writer, indentationLevel)
        {
            _namespace = ns;
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

            // Some attributes are named "None" in C#, which is a keyword in Python
            if (property.Name == "None")
            {
                Write("# Cannot convert to Python: ");
            }

            Write(property.Name);

            if (property.Type != null)
            {
                Write($": {property.Type.ToString(_namespace)}");
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

            WriteLine($"def {property.Name}(self) -> {property.Type.ToString(_namespace)}:");

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

            WriteLine($"def {property.Name}(self, value: {property.Type.ToString(_namespace)}):");

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

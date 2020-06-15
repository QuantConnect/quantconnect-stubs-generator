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
            if (property.Value == null)
            {
                RenderProperty(property);
            }
            else
            {
                RenderEnumMember(property);
            }
        }

        private void RenderProperty(Property property)
        {
            WriteLine("@property");
            WriteLine($"def {property.Name}(self) -> {property.Type.ToString(_class.Type.Namespace)}:");

            if (property.Summary != null)
            {
                WriteLine($"\"\"\"\n{property.Summary}\n\"\"\"".Indent());
            }

            WriteLine("pass".Indent());
            WriteLine();

            if (property.ReadOnly)
            {
                return;
            }

            WriteLine();

            WriteLine($"@{property.Name}.setter");
            WriteLine($"def {property.Name}(self, value: {property.Type.ToString(_class.Type.Namespace)}):");

            if (property.Summary != null)
            {
                WriteLine($"\"\"\"\n{property.Summary}\n\"\"\"".Indent());
            }

            WriteLine("pass".Indent());
            WriteLine();
        }

        private void RenderEnumMember(Property property)
        {
            if (property.Summary != null)
            {
                WriteLine($"\"\"\"\n{property.Summary}\n\"\"\"");
            }

            WriteLine($"{property.Name} = {property.Value}");
            WriteLine();
        }
    }
}

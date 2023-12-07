using System.IO;
using System.Linq;
using QuantConnectStubsGenerator.Model;

namespace QuantConnectStubsGenerator.Renderer
{
    public class EnumImportRenderer : ObjectRenderer<Class>
    {
        public EnumImportRenderer(StreamWriter writer, int indentationLevel) : base(writer, indentationLevel)
        {
        }

        public override void Render(Class cls)
        {
            WriteLine($"from . import {cls.Type.Name.Split('.').Last()}");
        }
    }
}

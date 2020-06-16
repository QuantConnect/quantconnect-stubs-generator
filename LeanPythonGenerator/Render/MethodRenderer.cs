using System.IO;
using LeanPythonGenerator.Model;
using LeanPythonGenerator.Utility;

namespace LeanPythonGenerator.Render
{
    public class MethodRenderer : BaseRenderer<Method>
    {
        private readonly Class _class;

        public MethodRenderer(StreamWriter writer, int indentationLevel, Class cls) : base(writer, indentationLevel)
        {
            _class = cls;
        }

        public override void Render(Method method)
        {
            if (method.Static)
            {
                WriteLine("@staticmethod");
            }

            if (method.Abstract)
            {
                WriteLine("@abstractmethod");
            }

            Write($"def {method.Name}(");

            if (!method.Static)
            {
                Write("self");
            }

            WriteLine($") -> {method.ReturnType.ToString(_class.Type.Namespace)}:");

            if (method.Summary != null)
            {
                WriteLine($"\"\"\"\n{method.Summary}\n\"\"\"".Indent());
            }

            WriteLine("pass".Indent());
            WriteLine();
        }
    }
}

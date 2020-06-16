using System.IO;
using LeanPythonGenerator.Model;
using LeanPythonGenerator.Utility;

namespace LeanPythonGenerator.Render
{
    public class MethodRenderer : BaseRenderer<Method>
    {
        private readonly Namespace _namespace;

        public MethodRenderer(StreamWriter writer, int indentationLevel, Namespace ns) : base(writer, indentationLevel)
        {
            _namespace = ns;
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

            if (method.Overload)
            {
                WriteLine("@overload");
            }

            Write($"def {method.Name}(");

            if (!method.Static)
            {
                Write("self");
            }

            WriteLine($") -> {method.ReturnType.ToString(_namespace)}:");

            if (method.Summary != null)
            {
                WriteLine($"\"\"\"\n{method.Summary}\n\"\"\"".Indent());
            }

            WriteLine("pass".Indent());
            WriteLine();
            WriteLine();
        }
    }
}

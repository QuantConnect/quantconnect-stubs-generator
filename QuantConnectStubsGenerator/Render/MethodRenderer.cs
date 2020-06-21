using System.IO;
using System.Linq;
using QuantConnectStubsGenerator.Utility;
using QuantConnectStubsGenerator.Model;

namespace QuantConnectStubsGenerator.Render
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

            if (method.Parameters.Count > 0)
            {
                if (!method.Static)
                {
                    Write(", ");
                }

                Write(string.Join(", ", method.Parameters.Select(ParameterToString)));
            }

            WriteLine($") -> {method.ReturnType.ToString(_namespace)}:");

            if (method.Summary != null)
            {
                WriteLine($"\"\"\"\n{method.Summary}\n\"\"\"".Indent());
            }

            WriteLine("...".Indent());
            WriteLine();
            WriteLine();
        }

        private string ParameterToString(Parameter parameter)
        {
            var str = $"{parameter.Name}: {parameter.Type.ToString(_namespace)}";

            if (parameter.VarArgs)
            {
                str = "*" + str;
            }

            if (parameter.Value != null)
            {
                str += $" = {parameter.Value}";
            }

            return str;
        }
    }
}

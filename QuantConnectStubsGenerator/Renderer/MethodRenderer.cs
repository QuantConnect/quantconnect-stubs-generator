using System.Collections.Generic;
using System.IO;
using System.Linq;
using QuantConnectStubsGenerator.Model;
using QuantConnectStubsGenerator.Utility;

namespace QuantConnectStubsGenerator.Renderer
{
    public class MethodRenderer : ObjectRenderer<Method>
    {
        public MethodRenderer(StreamWriter writer, int indentationLevel) : base(writer, indentationLevel)
        {
        }

        public override void Render(Method method)
        {
            if (method.Static)
            {
                WriteLine("@staticmethod");
            }

            if (method.Overload)
            {
                WriteLine("@typing.overload");
            }

            // In C# abstract methods and method overloads can be mixed freely
            // In Python this is not the case, overloaded abstract methods or
            // overloaded methods of which only some are abstract are not parsed the same in Python
            // For this reason @abc.abstractmethod is not added to abstract methods

            var args = new List<string>();

            if (!method.Static)
            {
                args.Add("self");
            }

            args.AddRange(method.Parameters.Select(ParameterToString));
            var argsStr = string.Join(", ", args);

            WriteLine($"def {method.Name}({argsStr}) -> {method.ReturnType.ToPythonString()}:");
            WriteSummary(method.Summary, true);
            WriteLine("...".Indent());

            WriteLine();
        }

        private string ParameterToString(Parameter parameter)
        {
            var str = $"{parameter.Name}: {parameter.Type.ToPythonString()}";

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

using System.Collections.Generic;
using System.IO;
using System.Linq;
using Python.Runtime;
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
            var snakeCasedMethod = GetSnakeCasedMethod(method);
            if (snakeCasedMethod.Name != method.Name)
            {
                Render(snakeCasedMethod);
                return;
            }

            if (method.Static)
            {
                WriteLine("@staticmethod");
            }

            if (method.Overload)
            {
                WriteLine("@overload");
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

            // PyCharm has several issues with warnings.warn() calls in overloaded methods
            //
            // Example 1:
            // def my_method() -> None: warnings.warn("Reason 1")
            // def my_method(var: int) -> None: warnings.warn("Reason 2")
            //
            // Example 2:
            // def my_method() -> None: warnings.warn("Reason 1")
            // def my_method(var: int) -> None: ...
            //
            // In both examples PyCharm will flag "my_method(2)" as being deprecated with message "Reason 1"
            // We therefore only add warnings.warn() to non-overloaded deprecated methods
            if (method.DeprecationReason != null && !method.Overload)
            {
                WriteLine($"warnings.warn(\"{method.DeprecationReason}\", DeprecationWarning)".Indent());
            }
            else
            {
                WriteLine("...".Indent());
            }

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

        private static Method GetSnakeCasedMethod(Method method)
        {
            var snakeCasedMethod = new Method(method.Name.ToSnakeCase(), method.ReturnType)
            {
                Static = method.Static,
                Overload = method.Overload,
                Summary = method.Summary,
                File = method.File,
                DeprecationReason = method.DeprecationReason
            };

            foreach (var parameter in method.Parameters)
            {
                snakeCasedMethod.Parameters.Add(new Parameter(parameter.Name.ToSnakeCase(), parameter.Type)
                {
                    VarArgs = parameter.VarArgs,
                    Value = parameter.Value
                });
            }

            return snakeCasedMethod;
        }
    }
}

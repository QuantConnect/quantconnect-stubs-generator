/*
 * QUANTCONNECT.COM - Democratizing Finance, Empowering Individuals.
 * Lean Algorithmic Trading Engine v2.0. Copyright 2014 QuantConnect Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
*/

using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using QuantConnectStubsGenerator.Model;
using QuantConnectStubsGenerator.Utility;

namespace QuantConnectStubsGenerator.Renderer
{
    public class MethodRenderer : ObjectRenderer<Method>
    {
        public MethodRenderer(TextWriter writer, int indentationLevel, ParseContext context)
            : base(writer, indentationLevel, context)
        {
        }

        public override void Render(Method method)
        {
            var snakeCasedMethod = GetSnakeCasedMethod(method);
            if (snakeCasedMethod != null)
            {
                method = snakeCasedMethod;
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
            var snakeCasedMethodName = method.Name.ToSnakeCase();
            if (snakeCasedMethodName.IsPythonReservedWord())
            {
                return null;
            }

            var snakeCasedMethod = new Method(snakeCasedMethodName, method.ReturnType)
            {
                Static = method.Static,
                Overload = method.Overload,
                File = method.File,
                DeprecationReason = method.DeprecationReason,
                Class = method.Class
            };

            var summary = method.Summary;

            foreach (var parameter in method.Parameters)
            {
                if (parameter.Name.StartsWith("*"))
                {
                    return method;
                }
                var snakeCasedParameterName = parameter.Name.ToSnakeCase();
                if (snakeCasedParameterName.IsPythonReservedWord())
                {
                    return null;
                }

                snakeCasedMethod.Parameters.Add(new Parameter(snakeCasedParameterName, parameter.Type)
                {
                    VarArgs = parameter.VarArgs,
                    Value = parameter.Value
                });

                if (summary != null)
                {
                    summary = Regex.Replace(summary, @$"\b{parameter.Name}\b", snakeCasedParameterName);
                }
            }

            snakeCasedMethod.Summary = summary;

            return snakeCasedMethod;
        }
    }
}


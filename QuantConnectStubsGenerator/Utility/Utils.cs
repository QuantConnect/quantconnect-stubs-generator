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

using QuantConnectStubsGenerator.Model;

namespace QuantConnectStubsGenerator.Utility
{
    public static class Utils
    {
        public static Parameter NormalizeParameter(Parameter parameter)
        {
            if (!IsListType(parameter.Type))
            {
                return parameter;
            }

            return new Parameter(parameter)
            {
                Type = NormalizeType(parameter.Type)
            };
        }

        public static PythonType NormalizeType(PythonType type)
        {
            if (!IsListType(type))
            {
                return type;
            }

            return new PythonType("Iterable", "typing")
            {
                TypeParameters = { NormalizeType(type.TypeParameters[0]) }
            };
        }

        public static bool IsListType(PythonType type)
        {
            return type.Namespace == "System.Collections.Generic" &&
                type.TypeParameters.Count == 1 &&
                (type.Name == "IReadOnlyCollection" || type.Name == "IEnumerable" || type.Name == "IList" || type.Name == "List");
        }
    }
}


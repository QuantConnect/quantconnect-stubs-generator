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
using System.Collections.Generic;
using System;

namespace QuantConnectStubsGenerator.Utility
{
    public static class Extensions
    {
        private static bool TryGetClass(PythonType classType, ParseContext context, out Class @class)
        {
            @class = null;
            if (classType == null)
            {
                return false;
            }

            try
            {
                var @namespace = context.GetNamespaceByName(classType.Namespace);
                @class = @namespace.GetClassByType(classType);
                return true;
            }
            catch (ArgumentException)
            {
                // Class not found:
                //   - The type was converted to a Python type (e.g. DateTime -> datetime),
                //     so the class will not be found in any namespace, no need to check. Or,
                //   - The class is private or internal, it won't be found in the namespaces.
                return false;
            }
        }

        public static IEnumerable<Class> GetBaseClasses(this Class cls, ParseContext context)
        {
            var baseClassTypes = new Queue<PythonType>(cls.InheritsFrom);
            var checkedClassTypes = new HashSet<PythonType>();

            while (baseClassTypes.TryDequeue(out var baseClassType))
            {
                if (TryGetClass(baseClassType, context, out var baseClass))
                {
                    yield return baseClass;

                    checkedClassTypes.Add(baseClassType);

                    foreach (var baseBaseClass in baseClass.InheritsFrom)
                    {
                        if (!checkedClassTypes.Contains(baseBaseClass))
                        {
                            baseClassTypes.Enqueue(baseBaseClass);
                            checkedClassTypes.Add(baseBaseClass);
                        }
                    }
                }
            }
        }

        public static IEnumerable<Class> GetClassAndBaseClasses(this Class cls, ParseContext context)
        {
            yield return cls;
            foreach (var baseClass in cls.GetBaseClasses(context))
            {
                yield return baseClass;
            }
        }
    }
}


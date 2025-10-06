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
using System.Linq;

namespace QuantConnectStubsGenerator.Model
{
    public class Class : CodeEntity
    {
        public PythonType Type { get; }

        public bool Static { get; set; }
        public bool Interface { get; set; }

        public IList<PythonType> InheritsFrom { get; set; } = new List<PythonType>();
        public PythonType MetaClass { get; set; }

        public Class ParentClass { get; set; }
        public IList<Class> InnerClasses { get; } = new List<Class>();

        public IList<Property> Properties { get; } = new List<Property>();
        public HashSet<Method> Methods { get; } = new HashSet<Method>();
        public bool AvoidImplicitTypes { get; set; }

        public Class(PythonType type)
        {
            Type = type;
        }

        public IEnumerable<PythonType> GetUsedTypes()
        {
            var types = new HashSet<PythonType>();

            // Parse types recursively to properly return deep generics
            var typesToProcess = new Queue<PythonType>(GetUsedTypesToIterateOver());

            while (typesToProcess.Count > 0)
            {
                var currentType = typesToProcess.Dequeue();

                types.Add(currentType);

                foreach (var typeParameter in currentType.TypeParameters)
                {
                    typesToProcess.Enqueue(typeParameter);
                }
            }

            // Python classes with type parameters always extend typing.Generic[T, ...] where T = typing.TypeVar('T')
            if (Type.TypeParameters.Count > 0)
            {
                types.Add(new PythonType("Generic", "typing"));
                types.Add(new PythonType("TypeVar", "typing"));
            }

            // PropertyRenderer adds the @abc.abstractmethod decorator to abstract properties
            if (Properties.Any(p => !p.Static && p.Abstract))
            {
                types.Add(new PythonType("abstractmethod", "abc"));
            }

            // PropertyRenderer adds warnings.warn() to deprecated non-static properties
            if (Properties.Any(p => p.DeprecationReason != null && !p.Static))
            {
                types.Add(new PythonType("warn", "warnings"));
            }

            // MethodRenderer adds the @typing.overload decorator to overloaded methods
            if (Methods.Any(m => m.Overload))
            {
                types.Add(new PythonType("overload", "typing"));
            }

            // MethodRenderer adds warnings.warn() to non-overloaded deprecated methods
            if (Methods.Any(m => m.DeprecationReason != null && !m.Overload))
            {
                types.Add(new PythonType("warn", "warnings"));
            }

            foreach (var innerClass in InnerClasses)
            {
                foreach (var usedType in innerClass.GetUsedTypes())
                {
                    types.Add(usedType);
                }
            }

            return types;
        }

        public override string ToString()
        {
            return Type.ToString();
        }

        /// <summary>
        /// Returns the used types which need to be recursively iterated over in GetUsedTypes().
        /// </summary>
        private IEnumerable<PythonType> GetUsedTypesToIterateOver()
        {
            yield return Type;

            foreach (var inheritedType in InheritsFrom)
            {
                yield return inheritedType;
            }

            if (MetaClass != null)
            {
                yield return MetaClass;
            }

            foreach (var property in Properties)
            {
                if (property.Type != null)
                {
                    yield return property.Type;
                }
            }

            foreach (var method in Methods)
            {
                yield return method.ReturnType;

                foreach (var parameter in method.Parameters)
                {
                    yield return parameter.Type;
                }
            }
        }
    }
}


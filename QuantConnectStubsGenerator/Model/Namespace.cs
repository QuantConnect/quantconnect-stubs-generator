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

using System;
using System.Collections.Generic;
using System.Linq;

namespace QuantConnectStubsGenerator.Model
{
    public class Namespace
    {
        public string Name { get; }

        private readonly IDictionary<string, Class> _classes = new Dictionary<string, Class>();

        public Namespace(string name)
        {
            Name = name;
        }

        public IEnumerable<Class> GetClasses()
        {
            return _classes.Values;
        }

        public IEnumerable<Class> GetParentClasses()
        {
            return _classes.Values.Where(cls => cls.ParentClass == null);
        }

        public Class GetClassByType(PythonType type)
        {
            var key = GetClassKey(type);

            if (_classes.ContainsKey(key))
            {
                return _classes[key];
            }

            throw new ArgumentException($"No class has been registered with type '{type.ToPythonString()}'");
        }

        public bool HasClass(PythonType type)
        {
            return _classes.ContainsKey(GetClassKey(type));
        }

        public void RegisterClass(Class cls)
        {
            _classes[GetClassKey(cls)] = cls;
        }

        private string GetClassKey(PythonType type)
        {
            return $"{type.Namespace}.{type.Name}";
        }

        private string GetClassKey(Class cls)
        {
            return GetClassKey(cls.Type);
        }
    }
}


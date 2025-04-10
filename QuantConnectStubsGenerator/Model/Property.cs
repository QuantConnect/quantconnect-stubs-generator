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

namespace QuantConnectStubsGenerator.Model
{
    public class Property
    {
        public string Name { get; }

        public PythonType Type { get; set; }

        public bool Static { get; set; }

        public bool Abstract { get; set; }

        public bool Constant { get; set; }

        public string Value { get; set; }

        public string Summary { get; set; }

        public string DeprecationReason { get; set; }

        public bool HasSetter { get; set; }

        public Class Class { get; set; }

        public Property(string name)
        {
            Name = name;
        }

        public Property(Property template, string name)
        {
            Name = name;
            Type = template.Type;
            Static = template.Static;
            Abstract = template.Abstract;
            Constant = template.Constant;
            Value = template.Value;
            Summary = template.Summary;
            DeprecationReason = template.DeprecationReason;
            HasSetter = template.HasSetter;
            Class = template.Class;
        }
    }
}


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

namespace QuantConnectStubsGenerator.Model
{
    public class Parameter : IEquatable<Parameter>
    {
        public string Name { get; }
        public PythonType Type { get; set; }

        public bool VarArgs { get; set; }
        public string Value { get; set; }

        public Parameter(string name, PythonType type)
        {
            Name = name;
            Type = type;
        }

        public Parameter(Parameter other)
            : this(other.Name, other.Type)
        {
            VarArgs = other.VarArgs;
            Value = other.Value;
        }

        public bool Equals(Parameter other)
        {
            if (ReferenceEquals(null, other)) return false;
            if (ReferenceEquals(this, other)) return true;
            return Name == other.Name
                && Type.Equals(other.Type)
                && VarArgs == other.VarArgs
                && Value == other.Value;
        }

        public override bool Equals(object obj)
        {
            if (ReferenceEquals(null, obj)) return false;
            if (ReferenceEquals(this, obj)) return true;
            return obj.GetType() == GetType() && Equals((Parameter)obj);
        }

        public override int GetHashCode()
        {
            return HashCode.Combine(Name, Type, VarArgs, Value);
        }

        public override string ToString()
        {
            return $"{Name}: {Type}";
        }
    }
}


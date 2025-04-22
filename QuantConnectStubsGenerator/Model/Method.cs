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
    public class Method : IEquatable<Method>
    {
        public string Name { get; }
        public PythonType ReturnType { get; set; }

        public bool Static { get; set; }
        public bool Overload { get; set; }

        public string Summary { get; set; }

        public string File { get; set; }

        public bool IsGeneric => GenericType != null;

        public PythonType GenericType { get; set; }

        public string DeprecationReason { get; set; }

        public IList<Parameter> Parameters { get; }

        public Class Class { get; set; }

        public Method(string name, PythonType returnType)
        {
            Name = name;
            ReturnType = returnType;
            Parameters = new List<Parameter>();
        }
        public Method(string name, Method other) : this(name, other.ReturnType)
        {
            File = other.File;
            Static = other.Static;
            Summary = other.Summary;
            Overload = other.Overload;
            Parameters = other.Parameters;
            GenericType = other.GenericType;
            DeprecationReason = other.DeprecationReason;
        }

        public bool Equals(Method other)
        {
            if (ReferenceEquals(null, other)) return false;
            if (ReferenceEquals(this, other)) return true;
            return Name == other.Name
                && Class.Equals(other.Class)
                && Static == other.Static
                && Overload == other.Overload
                && GenericType == other.GenericType
                && Parameters.SequenceEqual(other.Parameters);
        }

        public override bool Equals(object obj)
        {
            if (ReferenceEquals(null, obj)) return false;
            if (ReferenceEquals(this, obj)) return true;
            return obj.GetType() == GetType() && Equals((Method)obj);
        }

        public override int GetHashCode()
        {
            var hash = 19;
            foreach (var parameter in Parameters)
            {
                hash = hash * 31 + parameter.GetHashCode();
            }

            return HashCode.Combine(Name, Static, Overload, Class, GenericType, hash);
        }

        public override string ToString()
        {
            var genericRepr = IsGeneric ? $"[{GenericType}]" : string.Empty;
            return $"{Name}{genericRepr}({string.Join(", ", Parameters)}) -> {ReturnType}";
        }
    }
}


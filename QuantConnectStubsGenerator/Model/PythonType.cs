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
    public class PythonType : IEquatable<PythonType>
    {
        public string Name { get; set; }
        public string Namespace { get; set; }

        public string Alias { get; set; }
        public bool IsNamedTypeParameter { get; set; }

        public IList<PythonType> TypeParameters { get; set; } = new List<PythonType>();

        public PythonType(string name, string ns = null)
        {
            Name = name;
            Namespace = ns;
        }

        public string GetBaseName()
        {
            return Name.Contains('.') ? Name.Substring(0, Name.IndexOf('.')) : Name;
        }

        public string ToPythonString(bool ignoreAlias = false)
        {
            if (!ignoreAlias && Alias != null)
            {
                return Alias;
            }

            if (IsNamedTypeParameter)
            {
                return $"{Namespace}_{Name}".Replace('.', '_');
            }

            var str = "";

            if (Namespace != null)
            {
                str += $"{Namespace}.";
            }

            str += Name;

            if (TypeParameters.Count == 0)
            {
                return str;
            }

            str += "[";

            // Callable requires Callable[[ParameterType1, ParameterType2, ...], ReturnType]
            if (Namespace == "typing" && Name == "Callable")
            {
                str += "[";
                str += string.Join(
                    ", ",
                    TypeParameters.SkipLast(1).Select(type => type.ToPythonString()));
                str += "], ";
                str += TypeParameters.Last().ToPythonString();
            }
            else
            {
                str += string.Join(", ", TypeParameters.Select(type => type.ToPythonString()));
            }

            str += "]";

            return str;
        }

        public bool Equals(PythonType other)
        {
            if (ReferenceEquals(null, other)) return false;
            if (ReferenceEquals(this, other)) return true;
            return Name == other.Name
                   && Namespace == other.Namespace
                   && Alias == other.Alias
                   && IsNamedTypeParameter == other.IsNamedTypeParameter;
        }

        public override bool Equals(object obj)
        {
            if (ReferenceEquals(null, obj)) return false;
            if (ReferenceEquals(this, obj)) return true;
            return obj.GetType() == GetType() && Equals((PythonType) obj);
        }

        public override int GetHashCode()
        {
            return HashCode.Combine(Name, Namespace, Alias, IsNamedTypeParameter);
        }
    }
}


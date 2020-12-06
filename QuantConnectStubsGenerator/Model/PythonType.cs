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

        public bool IsAction { get; set; }

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
                if (IsAction)
                {
                    str += "[";
                    str += string.Join(", ", TypeParameters.Select(type => type.ToPythonString()));
                    str += "], None";
                }
                else
                {
                    str += "[";
                    str += string.Join(
                        ", ",
                        TypeParameters.SkipLast(1).Select(type => type.ToPythonString()));
                    str += "], ";
                    str += TypeParameters.Last().ToPythonString();
                }
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

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

        public IList<PythonType> TypeParameters { get; } = new List<PythonType>();

        public PythonType(string name, string ns = null)
        {
            Name = name;
            Namespace = ns;
        }

        public string ToPythonString(Namespace currentNamespace = null, bool ignoreAlias = false)
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

            if (Namespace != null && Namespace != currentNamespace?.Name)
            {
                str += $"{Namespace}.";
            }

            str += Name;

            if (TypeParameters.Count == 0)
            {
                return str;
            }

            str += "[";

            // Callable requires all type parameters but the last to be in a list
            if (Namespace == "typing" && Name == "Callable")
            {
                str += "[";
                str += string.Join(
                    ", ",
                    TypeParameters.SkipLast(1).Select(type => type.ToPythonString(currentNamespace)));
                str += "], ";
                str += TypeParameters.Last().ToPythonString(currentNamespace);
            }
            else
            {
                str += string.Join(", ", TypeParameters.Select(type => type.ToPythonString(currentNamespace)));
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

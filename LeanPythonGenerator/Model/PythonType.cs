using System;
using System.Collections.Generic;
using System.Linq;

namespace LeanPythonGenerator.Model
{
    public class PythonType : IEquatable<PythonType>
    {
        public string Name { get; }
        public string Namespace { get; }
        public IList<PythonType> TypeParameters { get; } = new List<PythonType>();

        public PythonType(string name, string ns = null)
        {
            Name = name;
            Namespace = ns;
        }

        public string ToString(string currentNamespace = "")
        {
            // Quote all non-imported types because there may be forward references
            var str = Namespace == currentNamespace ? $"'{Name}'" : Name;

            if (TypeParameters.Count == 0)
            {
                return str;
            }

            str += "[";
            str += string.Join(", ", TypeParameters.Select(type => type.ToString(currentNamespace)));
            str += "]";

            return str;
        }

        public bool Equals(PythonType other)
        {
            if (ReferenceEquals(null, other)) return false;
            if (ReferenceEquals(this, other)) return true;
            return Name == other.Name && Namespace == other.Namespace;
        }

        public override bool Equals(object obj)
        {
            if (ReferenceEquals(null, obj)) return false;
            if (ReferenceEquals(this, obj)) return true;
            return obj.GetType() == GetType() && Equals((PythonType) obj);
        }

        public override int GetHashCode()
        {
            return HashCode.Combine(Name, Namespace);
        }
    }
}

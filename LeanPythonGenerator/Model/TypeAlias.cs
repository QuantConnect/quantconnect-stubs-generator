using System;

namespace LeanPythonGenerator.Model
{
    public class TypeAlias : IEquatable<TypeAlias>
    {
        public string Alias { get; }
        public PythonType ActualType { get; }

        public TypeAlias(string alias, PythonType actualType)
        {
            Alias = alias;
            ActualType = actualType;
        }

        public bool Equals(TypeAlias other)
        {
            if (ReferenceEquals(null, other)) return false;
            if (ReferenceEquals(this, other)) return true;
            return Alias == other.Alias;
        }

        public override bool Equals(object obj)
        {
            if (ReferenceEquals(null, obj)) return false;
            if (ReferenceEquals(this, obj)) return true;
            return obj.GetType() == GetType() && Equals((TypeAlias) obj);
        }

        public override int GetHashCode()
        {
            return (Alias != null ? Alias.GetHashCode() : 0);
        }
    }
}

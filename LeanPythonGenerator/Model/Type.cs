using System.Collections.Generic;
using System.Linq;

namespace LeanPythonGenerator.Model
{
    public class Type
    {
        public string Name { get; }
        public string Namespace { get; }
        public IList<Type> TypeParameters { get; } = new List<Type>();

        public Type(string name, string ns = null)
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
    }
}

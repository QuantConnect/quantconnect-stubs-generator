using System.Collections.Generic;

namespace LeanPythonGenerator.Model
{
    public class Namespace
    {
        public string Name { get; }

        /// <summary>
        /// Types used within any class in the namespace.
        /// </summary>
        public ISet<Type> UsedTypes { get; } = new HashSet<Type>();

        public ISet<string> TypeParameterNames { get; } = new HashSet<string>();

        private readonly IDictionary<string, Class> _classes = new Dictionary<string, Class>();

        public Namespace(string name)
        {
            Name = name;
        }

        public IEnumerable<Class> GetClasses()
        {
            return _classes.Values;
        }

        public Class GetClassByType(Type type)
        {
            if (!_classes.ContainsKey(type.Name))
            {
                _classes[type.Name] = new Class(type);
            }

            return _classes[type.Name];
        }
    }
}

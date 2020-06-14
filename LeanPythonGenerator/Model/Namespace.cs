using System.Collections.Generic;

namespace LeanPythonGenerator.Model
{
    public class Namespace
    {
        public string Name { get; }

        private readonly IDictionary<string, Class> _classes = new Dictionary<string, Class>();

        public Namespace(string name)
        {
            Name = name;
        }

        public IEnumerable<Class> GetClasses()
        {
            return _classes.Values;
        }

        public Class GetClassByName(string name)
        {
            if (!_classes.ContainsKey(name))
            {
                _classes[name] = new Class(name, this);
            }

            return _classes[name];
        }
    }
}

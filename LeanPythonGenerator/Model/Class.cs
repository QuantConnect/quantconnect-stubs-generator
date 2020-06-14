using System.Collections.Generic;

namespace LeanPythonGenerator.Model
{
    public class Class
    {
        public Type Type { get; }

        public string Summary { get; set; }

        public ISet<Type> InheritsFrom { get; } = new HashSet<Type>();

        public Class ParentClass { get; set; }
        public IList<Class> InnerClasses { get; } = new List<Class>();

        public Class(Type type)
        {
            Type = type;
        }
    }
}

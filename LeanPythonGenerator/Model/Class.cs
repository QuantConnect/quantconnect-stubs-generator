using System.Collections.Generic;

namespace LeanPythonGenerator.Model
{
    public class Class
    {
        public Type Type { get; }

        public string Summary { get; set; }

        public IList<Type> InheritsFrom { get; } = new List<Type>();

        public Class ParentClass { get; set; }
        public IList<Class> InnerClasses { get; } = new List<Class>();

        public Class(Type type)
        {
            Type = type;
        }
    }
}

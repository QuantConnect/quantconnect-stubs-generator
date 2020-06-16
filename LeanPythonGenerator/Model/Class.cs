using System.Collections.Generic;

namespace LeanPythonGenerator.Model
{
    public class Class
    {
        public PythonType Type { get; }

        public string Summary { get; set; }

        public bool Static { get; set; }

        public ISet<PythonType> InheritsFrom { get; } = new HashSet<PythonType>();

        public Class ParentClass { get; set; }
        public IList<Class> InnerClasses { get; } = new List<Class>();

        public IList<Property> Properties { get; } = new List<Property>();
        public IList<Method> Methods { get; } = new List<Method>();

        public bool Interface { get; set; }

        public Class(PythonType type)
        {
            Type = type;
        }
    }
}

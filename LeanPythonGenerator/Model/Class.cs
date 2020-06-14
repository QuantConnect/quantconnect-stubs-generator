using System.Collections.Generic;

namespace LeanPythonGenerator.Model
{
    public class Class
    {
        public string Name { get; }
        public Namespace Namespace { get; }

        public string Summary { get; set; }

        /// <summary>
        /// Types which this class inherits from ("def Name(InheritsFrom):").
        /// </summary>
        public IList<Type> InheritsFrom { get; } = new List<Type>();

        /// <summary>
        /// Types which have to be defined before this class can be defined.
        /// </summary>
        public IList<Type> RequiredTypes { get; set; } = new List<Type>();

        public Class ParentClass { get; set; }
        public IList<Class> InnerClasses { get; } = new List<Class>();

        public Class(string name, Namespace ns)
        {
            Name = name;
            Namespace = ns;
        }
    }
}

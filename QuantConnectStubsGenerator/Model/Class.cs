using System.Collections.Generic;

namespace QuantConnectStubsGenerator.Model
{
    public class Class
    {
        public PythonType Type { get; }

        public string Summary { get; set; }

        public bool Static { get; set; }
        public bool Interface { get; set; }

        public IList<PythonType> InheritsFrom { get; set; } = new List<PythonType>();
        public PythonType MetaClass { get; set; }

        public Class ParentClass { get; set; }
        public IList<Class> InnerClasses { get; } = new List<Class>();

        public IList<Property> Properties { get; } = new List<Property>();

        public Class(PythonType type)
        {
            Type = type;
        }

        public IEnumerable<PythonType> GetUsedTypes()
        {
            var types = new HashSet<PythonType>();

            // Parse types and inherited types recursively to handle deep generics
            var typesToProcess = new Queue<PythonType>();

            typesToProcess.Enqueue(Type);

            foreach (var inheritedType in InheritsFrom)
            {
                typesToProcess.Enqueue(inheritedType);
            }

            if (MetaClass != null)
            {
                typesToProcess.Enqueue(MetaClass);
            }

            foreach (var property in Properties)
            {
                if (property.Type != null)
                {
                    typesToProcess.Enqueue(property.Type);
                }

                if (property.Abstract)
                {
                    types.Add(new PythonType("abstractmethod", "abc"));
                }
            }

            while (typesToProcess.Count > 0)
            {
                var currentType = typesToProcess.Dequeue();

                types.Add(currentType);

                foreach (var typeParameter in currentType.TypeParameters)
                {
                    typesToProcess.Enqueue(typeParameter);
                }
            }

            // Python classes with type parameters always extend typing.Generic[T, ...] where T = typing.TypeVar('T')
            if (Type.TypeParameters.Count > 0)
            {
                types.Add(new PythonType("Generic", "typing"));
                types.Add(new PythonType("TypeVar", "typing"));
            }

            foreach (var innerClass in InnerClasses)
            {
                foreach (var usedType in innerClass.GetUsedTypes())
                {
                    types.Add(usedType);
                }
            }

            return types;
        }
    }
}

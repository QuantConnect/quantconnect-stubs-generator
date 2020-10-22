using System.Collections.Generic;
using System.Linq;

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
        public IList<Method> Methods { get; } = new List<Method>();

        public Class(PythonType type)
        {
            Type = type;
        }

        public IEnumerable<PythonType> GetUsedTypes()
        {
            var types = new HashSet<PythonType>();

            // Parse types recursively to properly return deep generics
            var typesToProcess = new Queue<PythonType>(GetUsedTypesToIterateOver());

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

            // PropertyRenderer adds the @abc.abstractmethod decorator to abstract properties
            if (Properties.Any(p => !p.Static && p.Abstract))
            {
                types.Add(new PythonType("abstractmethod", "abc"));
            }

            // MethodRenderer adds the @typing.overload decorator to overloaded methods
            if (Methods.Any(m => m.Overload))
            {
                types.Add(new PythonType("overload", "typing"));
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

        /// <summary>
        /// Returns the used types which need to be recursively iterated over in GetUsedTypes().
        /// </summary>
        private IEnumerable<PythonType> GetUsedTypesToIterateOver()
        {
            yield return Type;

            foreach (var inheritedType in InheritsFrom)
            {
                yield return inheritedType;
            }

            if (MetaClass != null)
            {
                yield return MetaClass;
            }

            foreach (var property in Properties)
            {
                if (property.Type != null)
                {
                    yield return property.Type;
                }
            }

            foreach (var method in Methods)
            {
                yield return method.ReturnType;

                foreach (var parameter in method.Parameters)
                {
                    yield return parameter.Type;
                }
            }
        }
    }
}

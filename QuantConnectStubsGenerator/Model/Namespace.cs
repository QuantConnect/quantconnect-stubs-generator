using System;
using System.Collections.Generic;
using System.Linq;

namespace QuantConnectStubsGenerator.Model
{
    public class Namespace
    {
        public string Name { get; }
        public bool IsEnum { get; }

        private readonly IDictionary<string, Class> _classes = new Dictionary<string, Class>();

        private readonly IDictionary<string, Class> _enums = new Dictionary<string, Class>();

        public Namespace(string name, bool isEnum = false)
        {
            Name = name;
            IsEnum = isEnum;
        }

        public IEnumerable<Class> GetClasses()
        {
            return _classes.Values;
        }

        public IEnumerable<Class> GetParentClasses()
        {
            return _classes.Values.Where(cls => cls.ParentClass == null || cls.IsEnum());
        }

        public Class GetClassByType(PythonType type)
        {
            var key = GetClassKey(type);

            if (_classes.ContainsKey(key))
            {
                return _classes[key];
            }

            throw new ArgumentException($"No class has been registered with type '{type.ToPythonString()}'");
        }

        public bool HasClass(PythonType type)
        {
            return _classes.ContainsKey(GetClassKey(type));
        }

        public void RegisterClass(Class cls)
        {
            _classes[GetClassKey(cls)] = cls;
        }

        public IEnumerable<Class> GetEnums()
        {
            return _enums.Values;
        }

        public void RegisterEnum(Class cls)
        {
            _enums[GetClassKey(cls)] = cls;
        }

        private string GetClassKey(PythonType type)
        {
            return $"{type.Namespace}.{type.Name}";
        }

        private string GetClassKey(Class cls)
        {
            return GetClassKey(cls.Type);
        }
    }
}

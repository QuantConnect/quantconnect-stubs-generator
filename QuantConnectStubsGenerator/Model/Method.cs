using System.Collections.Generic;

namespace QuantConnectStubsGenerator.Model
{
    public class Method
    {
        public string Name { get; }
        public PythonType ReturnType { get; set; }

        public bool Abstract { get; set; }
        public bool Static { get; set; }
        public bool Overload { get; set; }

        public string Summary { get; set; }

        public IList<Parameter> Parameters { get; } = new List<Parameter>();

        public Method(string name, PythonType returnType)
        {
            Name = name;
            ReturnType = returnType;
        }
    }
}

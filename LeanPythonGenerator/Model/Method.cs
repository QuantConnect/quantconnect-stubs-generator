namespace LeanPythonGenerator.Model
{
    public class Method
    {
        public string Name { get; }
        public PythonType ReturnType { get; }

        public bool Abstract { get; set; }
        public bool Static { get; set; }

        public string Summary { get; set; }

        public Method(string name, PythonType returnType)
        {
            Name = name;
            ReturnType = returnType;
        }
    }
}

namespace LeanPythonGenerator.Model
{
    public class Parameter
    {
        public string Name { get; }
        public PythonType Type { get; }

        public string Value { get; set; }
        public string Summary { get; set; }

        public Parameter(string name, PythonType type)
        {
            Name = name;
            Type = type;
        }
    }
}

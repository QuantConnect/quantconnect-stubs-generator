namespace LeanPythonGenerator.Model
{
    public class Parameter
    {
        public string Name { get; }
        public PythonType Type { get; set; }

        public bool VarArgs { get; set; }
        public string Value { get; set; }

        public Parameter(string name, PythonType type)
        {
            Name = name;
            Type = type;
        }
    }
}

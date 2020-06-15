namespace LeanPythonGenerator.Model
{
    public class Property
    {
        public string Name { get; }
        public PythonType Type { get; set; }
        public bool ReadOnly { get; set; }
        public string Value { get; set; }
        public string Summary { get; set; }

        public Property(string name)
        {
            Name = name;
        }
    }
}

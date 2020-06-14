namespace LeanPythonGenerator.Model
{
    public class Type
    {
        public string Name { get; }

        public string Namespace { get; }

        public Type(string name, string ns = null)
        {
            Name = name;
            Namespace = ns;
        }
    }
}

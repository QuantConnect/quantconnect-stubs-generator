namespace QuantConnectStubsGenerator.Model
{
    public class Property
    {
        public string Name { get; }

        public PythonType Type { get; set; }

        public bool Static { get; set; }

        public bool Abstract { get; set; }

        public bool Constant { get; set; }

        public string Value { get; set; }

        public string Summary { get; set; }

        public string DeprecationReason { get; set; }

        public bool HasSetter { get; set; }

        public Class Class { get; set; }

        public Property(string name)
        {
            Name = name;
        }

        public Property(Property template, string name)
        {
            Name = name;
            Type = template.Type;
            Static = template.Static;
            Abstract = template.Abstract;
            Constant = template.Constant;
            Value = template.Value;
            Summary = template.Summary;
            DeprecationReason = template.DeprecationReason;
            HasSetter = template.HasSetter;
            Class = template.Class;
        }
    }
}

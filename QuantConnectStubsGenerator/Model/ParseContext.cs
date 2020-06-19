using System.Collections.Generic;

namespace QuantConnectStubsGenerator.Model
{
    public class ParseContext
    {
        private readonly IDictionary<string, Namespace> _namespaces = new Dictionary<string, Namespace>();

        public IEnumerable<Namespace> GetNamespaces()
        {
            return _namespaces.Values;
        }

        public Namespace GetNamespaceByName(string name)
        {
            if (!_namespaces.ContainsKey(name))
            {
                _namespaces[name] = new Namespace(name);
            }

            return _namespaces[name];
        }

        public void RemoveNamespace(string name)
        {
            _namespaces.Remove(name);
        }
    }
}

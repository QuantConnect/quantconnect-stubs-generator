using System;
using System.Collections.Generic;

namespace QuantConnectStubsGenerator.Model
{
    /// <summary>
    /// The ParseContext is the root container which is filled with information gathered from the C# files.
    ///
    /// At the start of the program one instance of this class is created and passed to all parsers.
    /// The parsers are responsible for filling the ParseContext with all relevant information.
    /// Afterwards, this information is used by the renderers to create the necessary Python stubs.
    /// </summary>
    public class ParseContext
    {
        private readonly IDictionary<string, Namespace> _namespaces = new Dictionary<string, Namespace>();

        public IEnumerable<Namespace> GetNamespaces()
        {
            return _namespaces.Values;
        }

        public Namespace GetNamespaceByName(string name)
        {
            if (_namespaces.ContainsKey(name))
            {
                return _namespaces[name];
            }

            throw new ArgumentException($"No namespace has been registered with name '{name}'");
        }

        public bool HasNamespace(string name)
        {
            return _namespaces.ContainsKey(name);
        }

        public void RegisterNamespace(Namespace ns)
        {
            _namespaces[ns.Name] = ns;
        }
    }
}

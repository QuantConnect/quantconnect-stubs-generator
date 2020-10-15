using System;
using System.Collections.Generic;
using System.Linq;
using QuantConnectStubsGenerator.Model;
using QuikGraph;
using QuikGraph.Algorithms;

namespace QuantConnectStubsGenerator.Utility
{
    /// <summary>
    /// The DependencyGraph is used by the NamespaceRenderer as a sort of queue
    /// to render classes in such order to limit the amount of forward references.
    /// </summary>
    public class DependencyGraph
    {
        private readonly IDictionary<PythonType, Class> _classes = new Dictionary<PythonType, Class>();

        private readonly AdjacencyGraph<PythonType, Edge<PythonType>> _graph =
            new AdjacencyGraph<PythonType, Edge<PythonType>>();

        public void AddClass(Class cls)
        {
            _classes[cls.Type] = cls;
            _graph.AddVertex(cls.Type);
        }

        public void AddDependency(Class cls, PythonType type)
        {
            if (!_classes.ContainsKey(cls.Type))
            {
                throw new ArgumentException($"'{cls.Type.ToPythonString()}' has not been registered using AddClass");
            }

            // Only dependencies between the registered classes are considered
            if (!_classes.ContainsKey(type))
            {
                return;
            }

            _graph.AddEdge(new Edge<PythonType>(cls.Type, type));
        }

        public IEnumerable<Class> GetClassesInOrder()
        {
            return _graph.TopologicalSort().Select(type => _classes[type]).Reverse();
        }
    }
}

using System.Linq;
using NUnit.Framework;
using QuantConnectStubsGenerator.Model;
using QuantConnectStubsGenerator.Utility;

namespace QuantConnectStubsGenerator.Tests.Utility
{
    [TestFixture]
    public class DependencyGraphTests
    {
        [Test]
        public void GetClassesInOrderShouldReturnTheRegisteredClassesInSuchOrderToMinimizeForwardReferences()
        {
            var classA = new Class(new PythonType("A"));
            var classB = new Class(new PythonType("B"));
            var classC = new Class(new PythonType("C"));

            var dependencyGraph = new DependencyGraph();

            dependencyGraph.AddClass(classA);
            dependencyGraph.AddClass(classB);
            dependencyGraph.AddClass(classC);

            dependencyGraph.AddDependency(classA, classB.Type);
            dependencyGraph.AddDependency(classA, classC.Type);
            dependencyGraph.AddDependency(classB, classC.Type);

            var classes = dependencyGraph.GetClassesInOrder().ToList();

            Assert.AreEqual(3, classes.Count);

            Assert.AreEqual(classC, classes[0]);
            Assert.AreEqual(classB, classes[1]);
            Assert.AreEqual(classA, classes[2]);
        }
    }
}

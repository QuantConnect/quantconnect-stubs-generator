using System.Linq;
using NUnit.Framework;
using QuantConnectStubsGenerator.Model;

namespace QuantConnectStubsGenerator.Tests.Model
{
    [TestFixture]
    public class ClassTests
    {
        [Test]
        public void GetUsedTypesShouldReturnAllTypesInTheClassAndItsInnerClasses()
        {
            var parentCls = new Class(new PythonType("ParentClass", "QuantConnect"));
            var childCls = new Class(new PythonType("ChildClass", "QuantConnect"))
            {
                ParentClass = parentCls,
                MetaClass = new PythonType("ABCMeta", "abc")
            };

            parentCls.InnerClasses.Add(childCls);

            childCls.Type.TypeParameters.Add(new PythonType("ChildClass.T", "QuantConnect")
            {
                IsNamedTypeParameter = true
            });

            childCls.InheritsFrom.Add(new PythonType("Any", "typing"));

            childCls.Properties.Add(new Property("Property")
            {
                Type = new PythonType("PropertyType", "QuantConnect")
            });

            childCls.Methods.Add(new Method("Method", new PythonType("ReturnType", "QuantConnect"))
            {
                Parameters = {new Parameter("Parameter", new PythonType("ParameterType", "QuantConnect"))}
            });

            var usedTypes = parentCls.GetUsedTypes().ToList();

            Assert.AreEqual(10, usedTypes.Count);
            Assert.IsTrue(usedTypes.Any(t => t.Namespace == "QuantConnect" && t.Name == "ParentClass"));
            Assert.IsTrue(usedTypes.Any(t => t.Namespace == "QuantConnect" && t.Name == "ChildClass"));
            Assert.IsTrue(usedTypes.Any(t => t.Namespace == "QuantConnect" && t.Name == "ChildClass.T"));
            Assert.IsTrue(usedTypes.Any(t => t.Namespace == "QuantConnect" && t.Name == "PropertyType"));
            Assert.IsTrue(usedTypes.Any(t => t.Namespace == "QuantConnect" && t.Name == "ReturnType"));
            Assert.IsTrue(usedTypes.Any(t => t.Namespace == "QuantConnect" && t.Name == "ParameterType"));
            Assert.IsTrue(usedTypes.Any(t => t.Namespace == "typing" && t.Name == "Generic"));
            Assert.IsTrue(usedTypes.Any(t => t.Namespace == "typing" && t.Name == "TypeVar"));
            Assert.IsTrue(usedTypes.Any(t => t.Namespace == "typing" && t.Name == "Any"));
            Assert.IsTrue(usedTypes.Any(t => t.Namespace == "abc" && t.Name == "ABCMeta"));
        }
    }
}

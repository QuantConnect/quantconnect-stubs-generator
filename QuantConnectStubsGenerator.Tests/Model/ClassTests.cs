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

            var usedTypes = parentCls.GetUsedTypes().ToList();

            Assert.AreEqual(7, usedTypes.Count);
            Assert.IsTrue(usedTypes.Any(type => type.Namespace == "QuantConnect" && type.Name == "ParentClass"));
            Assert.IsTrue(usedTypes.Any(type => type.Namespace == "QuantConnect" && type.Name == "ChildClass"));
            Assert.IsTrue(usedTypes.Any(type => type.Namespace == "QuantConnect" && type.Name == "ChildClass.T"));
            Assert.IsTrue(usedTypes.Any(type => type.Namespace == "typing" && type.Name == "Generic"));
            Assert.IsTrue(usedTypes.Any(type => type.Namespace == "typing" && type.Name == "TypeVar"));
            Assert.IsTrue(usedTypes.Any(type => type.Namespace == "typing" && type.Name == "Any"));
            Assert.IsTrue(usedTypes.Any(type => type.Namespace == "abc" && type.Name == "ABCMeta"));
        }
    }
}

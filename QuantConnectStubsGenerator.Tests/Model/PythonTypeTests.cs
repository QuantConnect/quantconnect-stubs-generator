using NUnit.Framework;
using QuantConnectStubsGenerator.Model;

namespace QuantConnectStubsGenerator.Tests.Model
{
    [TestFixture, Category("Unit")]
    public class PythonTypeTests
    {
        [Test]
        public void ToPythonStringCorrectlyFormatsAlias()
        {
            var type = new PythonType("Any", "typing")
            {
                Alias = "AnyAlias"
            };

            Assert.AreEqual("AnyAlias", type.ToPythonString());
        }

        [Test]
        public void ToPythonStringCorrectlyIgnoresAlias()
        {
            var type = new PythonType("Any", "typing")
            {
                Alias = "AnyAlias"
            };

            Assert.AreEqual("typing.Any", type.ToPythonString(null, true));
        }

        [Test]
        public void ToPythonStringCorrectlyFormatsNamedTypeParameter()
        {
            var type = new PythonType("MyClass.TKey", "QuantConnect.Data")
            {
                IsNamedTypeParameter = true
            };

            Assert.AreEqual("QuantConnect_Data_MyClass_TKey", type.ToPythonString());
        }

        [Test]
        public void ToPythonStringCorrectlyAddsNamespaceWhenNecessary()
        {
            var type = new PythonType("MyClass", "QuantConnect");

            Assert.AreEqual("QuantConnect.MyClass", type.ToPythonString(new Namespace("NotQuantConnect")));
        }

        [Test]
        public void ToPythonStringOmitsNamespaceWhenSameAsCurrentNamespace()
        {
            var type = new PythonType("MyClass", "QuantConnect");

            Assert.AreEqual("MyClass", type.ToPythonString(new Namespace("QuantConnect")));
        }

        [Test]
        public void ToPythonStringOmitsNamespaceWhenNamespaceIsNull()
        {
            var type = new PythonType("MyClass");

            Assert.AreEqual("MyClass", type.ToPythonString());
        }

        [Test]
        public void ToPythonStringCorrectlyFormatsTypeParameters()
        {
            var type = new PythonType("MyClass", "QuantConnect");
            type.TypeParameters.Add(new PythonType("MyOtherClass", "QuantConnect"));
            type.TypeParameters.Add(new PythonType("MyOtherClass2", "QuantConnect"));

            Assert.AreEqual(
                "QuantConnect.MyClass[QuantConnect.MyOtherClass, QuantConnect.MyOtherClass2]",
                type.ToPythonString());
        }

        [Test]
        public void ToPythonStringCorrectlyFormatsCallable()
        {
            var type = new PythonType("Callable", "typing");
            type.TypeParameters.Add(new PythonType("str"));
            type.TypeParameters.Add(new PythonType("str"));
            type.TypeParameters.Add(new PythonType("str"));

            Assert.AreEqual("typing.Callable[[str, str], str]", type.ToPythonString());
        }
    }
}

using System;
using System.Linq;
using NUnit.Framework;
using QuantConnectStubsGenerator.Model;

namespace QuantConnectStubsGenerator.Tests.Model
{
    [TestFixture]
    public class NamespaceTests
    {
        [Test]
        public void GetClassesShouldReturnAllRegisteredClasses()
        {
            var ns = new Namespace("Test");

            var parentCls = new Class(new PythonType("ParentClass", "QuantConnect"));
            var childCls = new Class(new PythonType("ChildClass", "QuantConnect"))
            {
                ParentClass = parentCls
            };

            parentCls.InnerClasses.Add(childCls);

            ns.RegisterClass(parentCls);
            ns.RegisterClass(childCls);

            var classes = ns.GetClasses().ToList();

            Assert.AreEqual(2, classes.Count);
            Assert.AreEqual(parentCls, classes[0]);
            Assert.AreEqual(childCls, classes[1]);
        }

        [Test]
        public void GetParentClassesShouldReturnAllRegisteredParentClasses()
        {
            var ns = new Namespace("Test");

            var parentCls = new Class(new PythonType("ParentClass", "QuantConnect"));
            var childCls = new Class(new PythonType("ChildClass", "QuantConnect"))
            {
                ParentClass = parentCls
            };

            parentCls.InnerClasses.Add(childCls);

            ns.RegisterClass(parentCls);
            ns.RegisterClass(childCls);

            var parentClasses = ns.GetParentClasses().ToList();

            Assert.AreEqual(1, parentClasses.Count);
            Assert.AreEqual(parentCls, parentClasses[0]);
        }

        [Test]
        public void GetClassByTypeShouldReturnThePreviouslyRegisteredClass()
        {
            var ns = new Namespace("Test");
            var cls = new Class(new PythonType("MyClass", "QuantConnect"));
            ns.RegisterClass(cls);

            Assert.AreEqual(cls, ns.GetClassByType(cls.Type));
        }

        [Test]
        public void GetClassByTypeShouldThrowIfNotRegistered()
        {
            var ns = new Namespace("Test");

            Assert.Throws<ArgumentException>(() => ns.GetClassByType(new PythonType("MyClass", "QuantConnect")));
        }

        [Test]
        public void HasClassShouldReturnTrueIfClassHasBeenRegistered()
        {
            var ns = new Namespace("Test");
            var cls = new Class(new PythonType("MyClass", "QuantConnect"));
            ns.RegisterClass(cls);

            Assert.IsTrue(ns.HasClass(cls.Type));
        }

        [Test]
        public void HasClassShouldReturnFalseIfClassHasNotBeenRegistered()
        {
            var ns = new Namespace("Test");

            Assert.IsFalse(ns.HasClass(new PythonType("MyClass", "QuantConnect")));
        }
    }
}

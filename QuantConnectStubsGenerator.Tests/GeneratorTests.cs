/*
 * QUANTCONNECT.COM - Democratizing Finance, Empowering Individuals.
 * Lean Algorithmic Trading Engine v2.0. Copyright 2014 QuantConnect Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
*/

using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using NUnit.Framework;
using QuantConnectStubsGenerator.Model;
using System.Collections.Generic;
using System.Linq;

namespace QuantConnectStubsGenerator.Tests
{
    [TestFixture]
    public class GeneratorTests
    {
        [TestCase("public", true)]
        [TestCase("protected", true)]
        [TestCase("", false)]
        [TestCase("private", false)]
        public void Interfaces(string interfaceModifier, bool expected)
        {
            var testGenerator = new TestGenerator
            {
                Files = new()
            {
                { "Test.cs", $@"
using System;

namespace QuantConnect.Benchmarks
{{
    /// <summary>
    /// Specifies how to compute a benchmark for an algorithm
    /// </summary>
    {interfaceModifier} interface IBenchmark
    {{
        /// <summary>
        /// Evaluates this benchmark at the specified time
        /// </summary>
        /// <param name=""time"">The time to evaluate the benchmark at</param>
        /// <returns>The value of the benchmark at the specified time</returns>
        decimal Evaluate(DateTime time);

        DateTime TestProperty {{get;}}
    }}
}}" }
            }
            };

            var result = testGenerator.GenerateModelsPublic();

            var namespaces = result.GetNamespaces().ToList();
            Assert.AreEqual(2, namespaces.Count);

            var baseNameSpace = namespaces.Single(x => x.Name == "QuantConnect");
            var benchmarksNameSpace = namespaces.Single(x => x.Name == "QuantConnect.Benchmarks");

            if (!expected)
            {
                Assert.AreEqual(0, benchmarksNameSpace.GetClasses().Count());
                return;
            }
            var benchmark = benchmarksNameSpace.GetClasses().Single();

            Assert.AreEqual("Evaluate", benchmark.Methods.Single().Name);
            Assert.IsFalse(string.IsNullOrEmpty(benchmark.Methods.Single().Summary));

            Assert.AreEqual("TestProperty", benchmark.Properties.Single().Name);
            Assert.IsTrue(string.IsNullOrEmpty(benchmark.Properties.Single().Summary));
        }

        [TestCase("ConstProperty1", true)]
        [TestCase("ConstProperty2", true)]
        [TestCase("NonConstProperty1", false)]
        [TestCase("NonConstProperty2", false)]
        [TestCase("NonConstProperty3", false)]
        [TestCase("NonConstProperty4", false)]
        [TestCase("NonConstProperty5", false)]
        [TestCase("NonConstProperty6", false)]
        [TestCase("NonConstProperty7", false)]
        [TestCase("NonConstProperty8", false)]
        [TestCase("NonConstProperty9", false)]
        [TestCase("NonConstProperty10", false)]
        [TestCase("NonConstProperty11", false)]
        [TestCase("NonConstProperty12", false)]
        public void ConstantProperties(string propertyName, bool shouldBeConstant)
        {
            var testGenerator = new TestGenerator
            {
                Files = new()
                {
                    { "Test.cs", $@"
using System;

namespace QuantConnect.Properties
{{
    /// <summary>
    /// Specifies how to compute a benchmark for an algorithm
    /// </summary>
    public class PropertiesClass
    {{
        public static int ConstProperty1 => 1;

        public static int ConstProperty2 {{ get; }}

        public int NonConstProperty1 {{ get; set; }}

        public int NonConstProperty2 {{ get; protected set; }}

        public int NonConstProperty3 {{ get; private set; }}

        public int NonConstProperty4 {{ get; internal set; }}

        public int NonConstProperty5 {{ get; protected internal set; }}

        public static int NonConstProperty6 {{ get; private protected set; }}

        public static int NonConstProperty7 {{ get; set; }}

        public static int NonConstProperty8 {{ get; protected set; }}

        public static int NonConstProperty9 {{ get; private set; }}

        public static int NonConstProperty10 {{ get; internal set; }}

        public static int NonConstProperty11 {{ get; protected internal set; }}

        public int NonConstProperty12 => 1;
    }}
}}" }
            }
            };

            var result = testGenerator.GenerateModelsPublic();

            var namespaces = result.GetNamespaces().ToList();
            Assert.AreEqual(2, namespaces.Count);

            var baseNameSpace = namespaces.Single(x => x.Name == "QuantConnect");
            var propertiesNameSpace = namespaces.Single(x => x.Name == "QuantConnect.Properties");

            var propertiesClass = propertiesNameSpace.GetClasses().Single();

            Assert.AreEqual(14, propertiesClass.Properties.Count);

            var property = propertiesClass.Properties.Single(x => x.Name == propertyName);
            Assert.AreEqual(shouldBeConstant, property.Constant);
        }

        [Test]
        public void GenericMethods()
        {
            var testGenerator = new TestGenerator
            {
                Files = new()
                {
                    { "Test.cs", @"
namespace QuantConnect.GenericMethodsTest
{
    public class TestClass
    {
        public int History(string parameter)
        {
            return 1;
        }
        public T History<T>(T parameter)
        {
            return parameter;
        }
        public PyObject History<T>(int parameter)
        {
            return null;
        }
    }
}" }
            }
            };

            var result = testGenerator.GenerateModelsPublic();

            var namespaces = result.GetNamespaces().ToList();
            Assert.AreEqual(2, namespaces.Count);

            var baseNameSpace = namespaces.Single(x => x.Name == "QuantConnect");
            var testNameSpace = namespaces.Single(x => x.Name == "QuantConnect.GenericMethodsTest");

            // The generic-method workaround hoists two helper classes to the namespace level
            // (issue #82). TestClass keeps only the property; it has no History methods.
            var testClass = testNameSpace.GetClasses().Single(x => x.Type.Name == "TestClass");
            Assert.AreEqual(0, testClass.Methods.Count);
            Assert.AreEqual(0, testClass.InnerClasses.Count);
            Assert.IsNotNull(testClass.Properties.SingleOrDefault(x => x.Name == "History"));

            // The dispatch helper is non-generic and exposes __call__ + __getitem__.
            var indexableClass = testNameSpace.GetClasses().Single(x => x.Type.Name == "_TestClass_History");
            Assert.AreEqual(0, indexableClass.Type.TypeParameters?.Count ?? 0);
            Assert.IsNotNull(indexableClass.Methods.SingleOrDefault(x => x.Name == "__getitem__"));
            Assert.IsNotNull(indexableClass.Methods.SingleOrDefault(x => x.Name == "__call__"));

            // The typed helper is generic and holds the Sequence[T]-returning overloads.
            var typedClass = testNameSpace.GetClasses().Single(x => x.Type.Name == "_Typed_TestClass_History");
            Assert.AreNotEqual(0, typedClass.Type.TypeParameters?.Count ?? 0);
            Assert.AreEqual(2, typedClass.Methods.Count(x => x.Name == "__call__"));
        }

        [Test]
        public void GenericMethodsInStaticExtensionClass()
        {
            var testGenerator = new TestGenerator
            {
                Files = new()
                {
                    { "Test.cs", @"
namespace QuantConnect.GenericMethodsExtensionTest
{
    public static class TestExtensionsClass
    {
        public static int ExtensionMethod(this int target, string parameter)
        {
            return 1;
        }
        public static T ExtensionMethod<T>(this int target, T parameter)
        {
            return parameter;
        }
        public static PyObject ExtensionMethod<T>(this int target, int parameter)
        {
            return null;
        }
    }
}" }
                }
            };

            var result = testGenerator.GenerateModelsPublic();

            var namespaces = result.GetNamespaces().ToList();
            Assert.AreEqual(2, namespaces.Count);

            var baseNameSpace = namespaces.Single(x => x.Name == "QuantConnect");
            var testNameSpace = namespaces.Single(x => x.Name == "QuantConnect.GenericMethodsExtensionTest");

            // The extension class is registered as a static class.
            var extensionsClass = testNameSpace.GetClasses().Single(x => x.Type.Name == "TestExtensionsClass");
            Assert.IsTrue(extensionsClass.Static);
            Assert.AreEqual(0, extensionsClass.Methods.Count);
            Assert.AreEqual(0, extensionsClass.InnerClasses.Count);
            var property = extensionsClass.Properties.SingleOrDefault(x => x.Name == "ExtensionMethod");
            Assert.IsNotNull(property);
            Assert.IsTrue(property.Static);

            // The dispatch helper is non-generic and exposes __call__ + __getitem__.
            var indexableClass = testNameSpace.GetClasses().Single(x => x.Type.Name == "_TestExtensionsClass_ExtensionMethod");
            Assert.AreEqual(0, indexableClass.Type.TypeParameters?.Count ?? 0);
            Assert.IsNotNull(indexableClass.Methods.SingleOrDefault(x => x.Name == "__getitem__"));

            // The non-generic __call__ includes 'target' (the 'this' parameter) as its first parameter.
            var dispatchCall = indexableClass.Methods.Single(x => x.Name == "__call__");
            Assert.AreEqual(2, dispatchCall.Parameters.Count);
            Assert.AreEqual("target", dispatchCall.Parameters[0].Name);
            Assert.AreEqual("int", dispatchCall.Parameters[0].Type.Name);

            // The property type must be of the indexable helper class type
            Assert.AreEqual(property.Type, indexableClass.Type);

            // The typed helper is generic and holds the Sequence[T]-returning overloads.
            var typedClass = testNameSpace.GetClasses().Single(x => x.Type.Name == "_Typed_TestExtensionsClass_ExtensionMethod");
            Assert.AreNotEqual(0, typedClass.Type.TypeParameters?.Count ?? 0);
            Assert.AreEqual(2, typedClass.Methods.Count(x => x.Name == "__call__"));

            // Each typed __call__ also carries 'target' (the 'this' parameter) as its first parameter.
            foreach (var call in typedClass.Methods.Where(x => x.Name == "__call__"))
            {
                Assert.IsTrue(call.Parameters.Count >= 1);
                Assert.AreEqual("target", call.Parameters[0].Name);
                Assert.AreEqual("int", call.Parameters[0].Type.Name);
            }
        }

        [Test]
        public void OutParameters()
        {
            var testGenerator = new TestGenerator
            {
                Files = new()
                {
                    { "Test.cs", @"
namespace QuantConnect.OutParametersTest
{
    public class TestClass
    {
        public int TestMethod(int parameter, out string outParameter)
        {
            outParameter = parameter.ToString();
            return parameter;
        }
    }
}" }
            }
            };

            var result = testGenerator.GenerateModelsPublic();

            var namespaces = result.GetNamespaces().ToList();
            Assert.AreEqual(2, namespaces.Count);

            var baseNameSpace = namespaces.Single(x => x.Name == "QuantConnect");
            var testNameSpace = namespaces.Single(x => x.Name == "QuantConnect.OutParametersTest");

            var testClass = testNameSpace.GetClasses().Single();
            Assert.AreEqual("TestClass", testClass.Type.Name);

            var testMethod = testClass.Methods.Single();
            Assert.AreEqual("TestMethod", testMethod.Name);
            Assert.AreEqual(2, testMethod.Parameters.Count);

            // First parameter
            var parameter1 = testMethod.Parameters[0];
            Assert.AreEqual("parameter", parameter1.Name);
            Assert.AreEqual("int", parameter1.Type.Name);
            Assert.IsNull(parameter1.Type.Namespace);
            Assert.AreEqual(0, parameter1.Type.TypeParameters.Count);

            // Second parameter (out param)
            var outParameter = testMethod.Parameters[1];
            Assert.AreEqual("outParameter", outParameter.Name);
            Assert.AreEqual("Optional", outParameter.Type.Name);
            Assert.AreEqual("typing", outParameter.Type.Namespace);
            Assert.AreEqual(1, outParameter.Type.TypeParameters.Count);
            Assert.AreEqual("str", outParameter.Type.TypeParameters[0].Name);
            Assert.IsNull(outParameter.Type.TypeParameters[0].Namespace);

            // Return type
            var returnType = testMethod.ReturnType;
            Assert.AreEqual("Tuple", returnType.Name);
            Assert.AreEqual("typing", returnType.Namespace);
            Assert.AreEqual(2, returnType.TypeParameters.Count);
            Assert.AreEqual("int", returnType.TypeParameters[0].Name);
            Assert.IsNull(returnType.TypeParameters[0].Namespace);
            Assert.AreEqual("str", returnType.TypeParameters[1].Name);
            Assert.IsNull(returnType.TypeParameters[1].Namespace);
        }

        [Test]
        public void PropertiesWithProtectedSetter()
        {
            var testGenerator = new TestGenerator
            {
                Files = new()
                {
                    {
                        "Test.cs",
                        @"
namespace QuantConnect.Test
{
    public class TestClass
    {
        public int TestProperty { get; protected set; }
    }
}"
                    }
                }
            };

            var result = testGenerator.GenerateModelsPublic();

            var namespaces = result.GetNamespaces().ToList();
            Assert.AreEqual(2, namespaces.Count);

            var baseNameSpace = namespaces.Single(x => x.Name == "QuantConnect");
            var testNameSpace = namespaces.Single(x => x.Name == "QuantConnect.Test");

            var testClass = testNameSpace.GetClasses().Single();
            Assert.AreEqual("TestClass", testClass.Type.Name);

            var testProperty = testClass.Properties.Single();
            Assert.AreEqual("TestProperty", testProperty.Name);
            Assert.IsTrue(testProperty.HasSetter);
        }

        [Test]
        public void CSharpEnumeratorsArePythonIterables()
        {
            var testGenerator = new TestGenerator
            {
                Files = new()
                {
                    {
                        "Test.cs",
                        @"
using System;
using System.Collections.Generic;

namespace QuantConnect.Test
{
    public class TestEnumerable : IEnumerable<int>
    {
        public IEnumerator<int> GetEnumerator()
        {
            yield return 1;
        }
        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }
    }
}"
                    }
                }
            };

            var result = testGenerator.GenerateModelsPublic();

            var ns = result.GetNamespaces().Single(x => x.Name == "QuantConnect.Test");
            var classes = ns.GetClasses().ToList();

            var testEnumerable = classes.Single(x => x.Type.Name == "TestEnumerable");
            var iterableBaseClassType = testEnumerable.InheritsFrom.SingleOrDefault(x => x.Name == "Iterable" && x.Namespace == "typing");
            Assert.IsNotNull(iterableBaseClassType);
            Assert.AreEqual(1, iterableBaseClassType.TypeParameters.Count);
            var itemType = iterableBaseClassType.TypeParameters[0];
            Assert.AreEqual(new PythonType("int"), itemType);
        }

        [Test]
        public void IterableOverloadsForEnumerableParameters()
        {
            var testGenerator = new TestGenerator
            {
                Files = new()
                {
                    {
                        "Test.cs",
                        @"
using System;
using System.Collections.Generic;

namespace QuantConnect.Test
{
    public class TestClass
    {
        public TestClass(List<int> enumerable)
        {
        }

        public TestClass(int someParam, IEnumerable<int> enumerable)
        {
        }

        public void Method1(IList<string> enumerable)
        {
        }

        public void Method2(IList<List<string>> enumerable)
        {
        }
    }
}"
                    }
                }
            };

            var result = testGenerator.GenerateModelsPublic();

            var ns = result.GetNamespaces().Single(x => x.Name == "QuantConnect.Test");
            var classes = ns.GetClasses().ToList();

            var testClass = classes.Single(x => x.Type.Name == "TestClass");

            var constructor1 = testClass.Methods.Where(x => x.Name == "__init__" && x.Parameters.Count == 1).Single();
            Assert.AreEqual("typing.List[int]", constructor1.Parameters[0].Type.ToPythonString());

            var constructor2 = testClass.Methods.Where(x => x.Name == "__init__" && x.Parameters.Count == 2).Single();
            // Enumerable parameters are always converted to List
            Assert.AreEqual("typing.List[int]", constructor2.Parameters[1].Type.ToPythonString());

            var method1 = testClass.Methods.Single(x => x.Name == "Method1");
            Assert.AreEqual("typing.List[str]", method1.Parameters[0].Type.ToPythonString());

            var method2 = testClass.Methods.Single(x => x.Name == "Method2");
            Assert.AreEqual("typing.List[typing.List[str]]", method2.Parameters[0].Type.ToPythonString());
        }

        [Test]
        public void GeneratesSetterForEvents()
        {
            var testGenerator = new TestGenerator
            {
                Files = new()
                {
                    {
                        "Test.cs",
                        @"
using System;

namespace QuantConnect.Test
{
    public class TestClass
    {
        private event EventHandler _event;

        public event EventHandler PublicPropertyEvent
        {
            add { _event += value; }
            remove { _event -= value; }
        }

        public event EventHandler PublicFieldEvent;

        protected event EventHandler ProtectedPropertyEvent
        {
            add { _event += value; }
            remove { _event -= value; }
        }

        protected event EventHandler ProtectedFieldEvent;

        private event EventHandler PrivatePropertyEvent
        {
            add { _event += value; }
            remove { _event -= value; }
        }

        private event EventHandler PrivateFieldEvent;

        internal event EventHandler InternalPropertyEvent
        {
            add { _event += value; }
            remove { _event -= value; }
        }

        internal event EventHandler InternalFieldEvent;
    }
}"
                    }
                }
            };

            var result = testGenerator.GenerateModelsPublic();

            var ns = result.GetNamespaces().Single(x => x.Name == "QuantConnect.Test");
            var classes = ns.GetClasses().ToList();
            var testClass = classes.Single(x => x.Type.Name == "TestClass");

            var publicPropertyEvent = testClass.Properties.Single(x => x.Name == "PublicPropertyEvent");
            Assert.IsTrue(publicPropertyEvent.HasSetter);

            var publicFieldEvent = testClass.Properties.Single(x => x.Name == "PublicFieldEvent");
            Assert.IsTrue(publicFieldEvent.HasSetter);

            var protectedPropertyEvent = testClass.Properties.Single(x => x.Name == "ProtectedPropertyEvent");
            Assert.IsTrue(protectedPropertyEvent.HasSetter);

            var protectedFieldEvent = testClass.Properties.Single(x => x.Name == "ProtectedFieldEvent");
            Assert.IsTrue(protectedFieldEvent.HasSetter);

            var privatePropertyEvent = testClass.Properties.SingleOrDefault(x => x.Name == "PrivatePropertyEvent");
            Assert.IsNull(privatePropertyEvent);

            var privateFieldEvent = testClass.Properties.SingleOrDefault(x => x.Name == "PrivateFieldEvent");
            Assert.IsNull(privateFieldEvent);

            var internalPropertyEvent = testClass.Properties.SingleOrDefault(x => x.Name == "InternalPropertyEvent");
            Assert.IsNull(internalPropertyEvent);

            var internalFieldEvent = testClass.Properties.SingleOrDefault(x => x.Name == "InternalFieldEvent");
            Assert.IsNull(internalFieldEvent);
        }

        [TestCase("implicit", true)]
        [TestCase("explicit", false)]
        public void StringConversionOperatorDeterminesStrInheritance(string keyword, bool shouldInheritFromStr)
        {
            var testGenerator = new TestGenerator
            {
                Files = new()
                {
                    { "TestClass.cs", $@"
namespace QuantConnect
{{
    public class TestClass
    {{
        public static {keyword} operator string(TestClass obj)
        {{
            return obj.ToString();
        }}
    }}
}}" }
                }
            };

            var result = testGenerator.GenerateModelsPublic();

            var testClass = result.GetNamespaceByName("QuantConnect").GetClasses().Single(c => c.Type.Name == "TestClass");

            Assert.AreEqual(shouldInheritFromStr, testClass.InheritsFrom.Any(t => t.Name == "str" && t.Namespace == null));
        }

        [TestCase("IExtendedDictionary", "QuantConnect.Interfaces", "keys", "typing.List[QuantConnect_Interfaces_IExtendedDictionary_TKey]")]
        [TestCase("IExtendedDictionary", "QuantConnect.Interfaces", "values", "typing.List[QuantConnect_Interfaces_IExtendedDictionary_TValue]")]
        [TestCase("ExtendedDictionary", "QuantConnect", "keys", "typing.List[QuantConnect_ExtendedDictionary_TKey]")]
        [TestCase("ExtendedDictionary", "QuantConnect", "values", "typing.List[QuantConnect_ExtendedDictionary_TValue]")]
        [TestCase("ExtendedDictionary", "QuantConnect", "items",
            "typing.List[typing.Tuple[QuantConnect_ExtendedDictionary_TKey, QuantConnect_ExtendedDictionary_TValue]]")]
        [TestCase("ExtendedDictionary", "QuantConnect", "popitem",
            "typing.Tuple[QuantConnect_ExtendedDictionary_TKey, QuantConnect_ExtendedDictionary_TValue]")]
        [TestCase("ExtendedDictionary", "QuantConnect", "copy",
            "typing.Dict[QuantConnect_ExtendedDictionary_TKey, QuantConnect_ExtendedDictionary_TValue]")]
        [TestCase("ExtendedDictionary", "QuantConnect", "fromkeys",
            "typing.Dict[QuantConnect_ExtendedDictionary_TKey, QuantConnect_ExtendedDictionary_TValue]")]
        [TestCase("ExtendedDictionary", "QuantConnect", "Remove", "bool")]
        public void ExtendedDictionaryPythonMethodsAreTypedWithKeyAndValueTypes(string className, string ns, string methodName,
            string expectedReturnType)
        {
            var testGenerator = new TestGenerator
            {
                Files = new()
                {
                    { "IExtendedDictionary.cs", @"
using Python.Runtime;

namespace QuantConnect.Interfaces
{
    public interface IExtendedDictionary<TKey, TValue>
    {
        PyList keys();
        PyList values();
    }
}" },
                    { "ExtendedDictionary.cs", @"
using Python.Runtime;
using QuantConnect.Interfaces;

namespace QuantConnect
{
    public abstract class ExtendedDictionary<TKey, TValue> : IExtendedDictionary<TKey, TValue>
    {
        public PyDict copy() => null;
        public PyDict fromkeys(TKey[] sequence) => null;
        public PyDict fromkeys(TKey[] sequence, TValue value) => null;
        public PyList items() => null;
        public PyTuple popitem() => null;
        public PyList keys() => null;
        public PyList values() => null;
        public bool Remove(TKey key) => false;
    }
}" }
                }
            };

            var result = testGenerator.GenerateModelsPublic();

            var cls = result.GetNamespaceByName(ns).GetClasses().Single(c => c.Type.Name == className);
            var methods = cls.Methods.Where(m => m.Name == methodName).ToList();

            Assert.IsNotEmpty(methods);
            foreach (var method in methods)
            {
                Assert.AreEqual(expectedReturnType, method.ReturnType.ToPythonString());
            }
        }

        [Test]
        public void BaseClassWithFewerGenericsResolvesToTheKeptVariant()
        {
            var testGenerator = new TestGenerator
            {
                Files = new()
                {
                    { "BaseDictionary.cs", @"
using System.Collections.Generic;

namespace QuantConnect.Util
{
    public class BaseDictionary<TKey, TValue, TDictionary>
        where TDictionary : IDictionary<TKey, TValue>
    {
    }

    public class BaseDictionary<TKey, TValue> : BaseDictionary<TKey, TValue, Dictionary<TKey, TValue>>
    {
    }
}" },
                    { "DerivedDictionary.cs", @"
using QuantConnect.Util;

namespace QuantConnect.Data
{
    public class DerivedDictionary<T> : BaseDictionary<string, T>
    {
    }
}" }
                }
            };

            var result = testGenerator.GenerateModelsPublic();

            var baseDictionary = result.GetNamespaceByName("QuantConnect.Util").GetClasses().Single();
            Assert.AreEqual(3, baseDictionary.Type.TypeParameters.Count);

            var derived = result.GetNamespaceByName("QuantConnect.Data").GetClasses().Single();
            Assert.AreEqual(
                "QuantConnect.Util.BaseDictionary[str, QuantConnect_Data_DerivedDictionary_T, System.Collections.Generic.Dictionary[str, QuantConnect_Data_DerivedDictionary_T]]",
                derived.InheritsFrom.Single().ToPythonString());
        }

        private const string ExtensionMethodsSource = @"
using System.Collections.Generic;

namespace QuantConnect.Orders
{
    public enum OrderStatus { New, Filled }

    public interface IShape { double Side { get; } }

    public class Square : IShape { public double Side => 2; }

    public class Model
    {
        public string Name { get; set; }
        public string Existing() => ""member"";
    }

    public class DerivedModel : Model { }

    public static class OrderExtensions
    {
        public static bool IsOpen(this OrderStatus status) => status != OrderStatus.Filled;
        public static string Describe(this OrderStatus status, string prefix, int times = 1) => prefix;
        public static double Area(this IShape shape) => shape.Side * shape.Side;
        public static string Describe(this Model model, string prefix = """") => prefix + model.Name;
        public static string Existing(this Model model) => ""extension"";
        public static T Identity<T>(this T value) => value;
        public static int Total(this List<int> values) => 0;
        public static string Twice(this string value) => value + value;
    }
}";

        [Test]
        public void ExtensionMethodsAreBoundToTheExtendedType()
        {
            var testGenerator = new TestGenerator { Files = new() { { "Test.cs", ExtensionMethodsSource } } };
            var ns = testGenerator.GenerateModelsPublic().GetNamespaceByName("QuantConnect.Orders");
            Class GetClass(string name) => ns.GetClasses().Single(cls => cls.Type.Name == name);

            var orderStatus = GetClass("OrderStatus");
            var isOpen = orderStatus.Methods.Single(method => method.Name == "IsOpen");
            Assert.IsFalse(isOpen.Static);
            Assert.AreEqual(0, isOpen.Parameters.Count);
            Assert.AreEqual("bool", isOpen.ReturnType.ToPythonString());

            // the instance is dropped, the remaining parameters keep their defaults
            var describe = orderStatus.Methods.Single(method => method.Name == "Describe");
            Assert.AreEqual(new[] { "prefix", "times" }, describe.Parameters.Select(parameter => parameter.Name).ToArray());
            Assert.AreEqual("1", describe.Parameters[1].Value);

            // interface targets are bound to the interface, implementing classes inherit them
            Assert.AreEqual(1, GetClass("IShape").Methods.Count(method => method.Name == "Area"));
            Assert.AreEqual(0, GetClass("Square").Methods.Count(method => method.Name == "Area"));

            // a real member wins over an extension with the same name
            var model = GetClass("Model");
            var existing = model.Methods.Single(method => method.Name == "Existing");
            Assert.IsNull(existing.ExtendedType);
            Assert.AreEqual(1, model.Methods.Count(method => method.Name == "Describe"));
            Assert.AreEqual(0, GetClass("DerivedModel").Methods.Count(method => method.Name == "Describe"));

            // generic and Python native targets are not bound anywhere
            var boundNames = ns.GetClasses().Where(cls => !cls.Static).SelectMany(cls => cls.Methods).Select(method => method.Name).ToList();
            Assert.IsFalse(boundNames.Contains("Identity"));
            Assert.IsFalse(boundNames.Contains("Total"));
            Assert.IsFalse(boundNames.Contains("Twice"));

            // the static forms stay available
            var extensions = GetClass("OrderExtensions");
            Assert.IsTrue(extensions.Methods.Where(method => method.Name == "IsOpen").All(method => method.Static && method.Parameters.Count == 1));
        }

        [Test]
        public void FrameworkExtensionMethodsAreNotBound()
        {
            var testGenerator = new TestGenerator
            {
                Files = new()
                {
                    { "Test.cs", @"
namespace System.Shapes
{
    public class Circle { }

    public static class CircleExtensions
    {
        public static double Area(this Circle circle) => 0;
    }
}" }
                }
            };

            var ns = testGenerator.GenerateModelsPublic().GetNamespaceByName("System.Shapes");
            var circle = ns.GetClasses().Single(cls => cls.Type.Name == "Circle");
            Assert.AreEqual(0, circle.Methods.Count(method => method.Name == "Area"));
        }

        [Test]
        public void ImplicitNumericConversionAddsTheNumberProtocol()
        {
            var testGenerator = new TestGenerator
            {
                Files = new()
                {
                    { "Test.cs", @"
namespace QuantConnect.Orders.Fees
{
    public class OrderFee
    {
        public decimal Amount { get; set; }
        public static implicit operator decimal(OrderFee fee) => fee.Amount;
    }

    public class Money
    {
        public decimal Amount { get; set; }
        public static implicit operator decimal(Money money) => money.Amount;
        public static Money operator +(Money a, Money b) => new Money();
    }

    public class Plain
    {
        public static implicit operator string(Plain plain) => """";
    }

    public class Wrapper
    {
        public static implicit operator decimal(int value) => value;
    }

    public class Ticket
    {
        [StubsIgnore]
        public static implicit operator int(Ticket ticket) => 0;
    }
}" }
                }
            };

            var ns = testGenerator.GenerateModelsPublic().GetNamespaceByName("QuantConnect.Orders.Fees");
            Class GetClass(string name) => ns.GetClasses().Single(cls => cls.Type.Name == name);
            string[] Signatures(Class cls, string name) => cls.Methods
                .Where(method => method.Name == name)
                .Select(method => $"{string.Join(",", method.Parameters.Select(parameter => parameter.Type.ToPythonString()))}->{method.ReturnType.ToPythonString()}")
                .OrderBy(signature => signature, System.StringComparer.Ordinal)
                .ToArray();

            var orderFee = GetClass("OrderFee");
            Assert.AreEqual(new[] { "QuantConnect.Orders.Fees.OrderFee->float", "float->float" }, Signatures(orderFee, "__add__"));
            Assert.AreEqual(new[] { "float->float" }, Signatures(orderFee, "__radd__"));
            Assert.AreEqual(new[] { "QuantConnect.Orders.Fees.OrderFee->float", "float->float" }, Signatures(orderFee, "__truediv__"));
            Assert.AreEqual(new[] { "QuantConnect.Orders.Fees.OrderFee->bool", "float->bool" }, Signatures(orderFee, "__lt__"));
            Assert.AreEqual(new[] { "->float" }, Signatures(orderFee, "__neg__"));
            Assert.AreEqual(new[] { "->float" }, Signatures(orderFee, "__float__"));
            Assert.AreEqual(new[] { "->int" }, Signatures(orderFee, "__int__"));

            // the type's own operator is kept, the others are synthesized
            var money = GetClass("Money");
            Assert.AreEqual(new[] { "QuantConnect.Orders.Fees.Money->QuantConnect.Orders.Fees.Money" }, Signatures(money, "__add__"));
            Assert.AreEqual(new[] { "QuantConnect.Orders.Fees.Money->float", "float->float" }, Signatures(money, "__sub__"));

            // conversions to a number from other types or marked as ignored do not count
            foreach (var name in new[] { "Plain", "Wrapper", "Ticket" })
            {
                Assert.IsFalse(GetClass(name).Methods.Any(method => method.Name.StartsWith("__") && method.Name != "__init__"), name);
            }
        }

        [Test]
        public void FrameworkTargetsAreNotBound()
        {
            // object, IEnumerable, IDisposable... are shared by countless classes, Python.NET does not bind their extensions
            var testGenerator = new TestGenerator
            {
                Files = new()
                {
                    { "Test.cs", @"
namespace System.Shapes
{
    public class Circle { }

    public interface IRound { }
}

namespace QuantConnect.Orders
{
    public class Square : System.Shapes.IRound { }

    public static class ShapeExtensions
    {
        public static double Area(this System.Shapes.Circle circle) => 0;
        public static double Roundness(this System.Shapes.IRound round) => 0;
    }
}" }
                }
            };

            var context = testGenerator.GenerateModelsPublic();
            Class GetClass(string ns, string name) => context.GetNamespaceByName(ns).GetClasses().Single(cls => cls.Type.Name == name);

            Assert.IsFalse(GetClass("System.Shapes", "Circle").Methods.Any(method => method.Name == "Area"));
            Assert.IsFalse(GetClass("System.Shapes", "IRound").Methods.Any(method => method.Name == "Roundness"));
            Assert.IsFalse(GetClass("QuantConnect.Orders", "Square").Methods.Any(method => method.Name == "Roundness"));

            // the static forms stay available
            var extensions = GetClass("QuantConnect.Orders", "ShapeExtensions");
            Assert.IsTrue(extensions.Methods.Where(method => method.Name is "Area" or "Roundness").All(method => method.Static && method.Parameters.Count == 1));
            Assert.AreEqual(2, extensions.Methods.Count(method => method.Name is "Area" or "Roundness"));
        }

        [Test]
        public void EditorBrowsableNeverExtensionMethodsKeepTheStaticFormOnly()
        {
            var testGenerator = new TestGenerator
            {
                Files = new()
                {
                    { "Test.cs", @"
using System.ComponentModel;

namespace QuantConnect.Orders
{
    public class Model { }

    public static class ModelExtensions
    {
        [EditorBrowsable(EditorBrowsableState.Never)]
        public static string Hidden(this Model model) => """";

        [System.ComponentModel.EditorBrowsable(System.ComponentModel.EditorBrowsableState.Never)]
        public static string HiddenQualified(this Model model) => """";

        [EditorBrowsable(EditorBrowsableState.Advanced)]
        public static string Advanced(this Model model) => """";
    }

    [EditorBrowsable(EditorBrowsableState.Never)]
    public static class HiddenModelExtensions
    {
        public static string HiddenByClass(this Model model) => """";
    }
}" }
                }
            };

            var ns = testGenerator.GenerateModelsPublic().GetNamespaceByName("QuantConnect.Orders");
            Class GetClass(string name) => ns.GetClasses().Single(cls => cls.Type.Name == name);

            var bound = GetClass("Model").Methods.Select(method => method.Name).ToList();
            Assert.AreEqual(new[] { "Advanced" }, bound.ToArray());

            // the static forms stay available, Python.NET still binds them on the static class
            Assert.IsTrue(GetClass("ModelExtensions").Methods.Single(method => method.Name == "Hidden").Static);
            Assert.IsTrue(GetClass("ModelExtensions").Methods.Single(method => method.Name == "HiddenQualified").Static);
            Assert.IsTrue(GetClass("HiddenModelExtensions").Methods.Single(method => method.Name == "HiddenByClass").Static);
        }

        [Test]
        public void DeclaredOrInheritedOperatorsAreNotSynthesizedInEitherDirection()
        {
            // Python.NET synthesizes an operator in both directions or not at all, a declared or inherited one wins in both
            var testGenerator = new TestGenerator
            {
                Files = new()
                {
                    { "Test.cs", @"
namespace QuantConnect.Data
{
    // declares + in one direction only, like MultiPeriodField
    public class Field
    {
        public static implicit operator decimal(Field field) => 0;
        public static decimal operator +(Field a, Field b) => 0;
    }

    public class BaseAmount
    {
        public static string operator -(BaseAmount a, BaseAmount b) => """";
    }

    public class DerivedAmount : BaseAmount
    {
        public static implicit operator decimal(DerivedAmount amount) => 0;
    }
}" }
                }
            };

            var ns = testGenerator.GenerateModelsPublic().GetNamespaceByName("QuantConnect.Data");
            Class GetClass(string name) => ns.GetClasses().Single(cls => cls.Type.Name == name);
            int Count(Class cls, string name) => cls.Methods.Count(method => method.Name == name);

            var field = GetClass("Field");
            Assert.AreEqual(1, Count(field, "__add__"));
            Assert.AreEqual(0, Count(field, "__radd__"));
            Assert.AreEqual(2, Count(field, "__sub__"));
            Assert.AreEqual(1, Count(field, "__rsub__"));

            var derived = GetClass("DerivedAmount");
            Assert.AreEqual(0, Count(derived, "__sub__"));
            Assert.AreEqual(0, Count(derived, "__rsub__"));
            Assert.AreEqual(2, Count(derived, "__add__"));
            Assert.AreEqual(1, Count(derived, "__radd__"));
        }

        internal class TestGenerator : Generator
        {
            public Dictionary<string, string> Files { get; set; }
            public TestGenerator() : base("/", "/", "/")
            {
            }

            protected override IEnumerable<SyntaxTree> GetSyntaxTrees()
            {
                foreach (var fileContent in Files)
                {
                    yield return CSharpSyntaxTree.ParseText(fileContent.Value, path: fileContent.Key);
                }
            }

            public ParseContext GenerateModelsPublic()
            {
                ParseContext context = new();

                base.GenerateModels(context);

                return context;
            }
        }
    }
}


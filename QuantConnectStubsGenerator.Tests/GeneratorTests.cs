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

            var testClass = testNameSpace.GetClasses().Single();
            Assert.AreEqual("TestClass", testClass.Type.Name);

            var testMethodCount = testClass.Methods.Count;
            Assert.AreEqual(0, testMethodCount);

            var innerClass = testClass.InnerClasses.Single();

            Assert.AreEqual(0, innerClass.Type.TypeParameters?.Count ?? 0);
            Assert.IsNotNull(innerClass.Methods.SingleOrDefault(x => x.Name == "__getitem__"));
            Assert.IsNotNull(innerClass.Methods.SingleOrDefault(x => x.Name == "__call__"));

            var innerInnerClass = innerClass.InnerClasses.Single();

            Assert.AreNotEqual(0, innerInnerClass.Type.TypeParameters?.Count ?? 0);
            Assert.AreEqual(2, innerInnerClass.Methods.Count(x => x.Name == "__call__"));
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
            Assert.AreEqual("typing.Iterable[int]", constructor2.Parameters[1].Type.ToPythonString());

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


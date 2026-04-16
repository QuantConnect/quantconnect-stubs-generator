/*
 * QUANTCONNECT.COM - Democratizing Finance, Empowering Individuals.
 * Lean Algorithmic Trading Engine v2.0. Copyright 2025 QuantConnect Corporation.
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

using System.Collections.Generic;
using System.Linq;
using NUnit.Framework;
using NUnit.Framework.Internal;
using QuantConnectStubsGenerator.Model;
using static QuantConnectStubsGenerator.Tests.GeneratorTests;

namespace QuantConnectStubsGenerator.Tests
{
    [TestFixture]
    public class MethodParserTests
    {
        [Test]
        public void ParamsHandling()
        {
            var testGenerator = new TestGenerator
            {
                Files = new()
                {
                    { "Test.cs", @"
namespace QuantConnect.MethodParserTests
{
    public class TestClass
    {
        public int ParamsTestMethod(params string[] tickers)
        {
            return 1;
        }
    }
}" }
            }
            };

            var result = testGenerator.GenerateModelsPublic();

            var namespaces = result.GetNamespaces().ToList();
            Assert.AreEqual(2, namespaces.Count);

            var baseNameSpace = namespaces.Single(x => x.Name == "QuantConnect");
            var testNameSpace = namespaces.Single(x => x.Name == "QuantConnect.MethodParserTests");

            var testClass = testNameSpace.GetClasses().Single();
            Assert.AreEqual("TestClass", testClass.Type.Name);

            var testMethodCount = testClass.Methods.Count;
            Assert.AreEqual(1, testMethodCount);

            var method = testClass.Methods.Single();

            Assert.AreEqual(1, method.Parameters.Count);
            Assert.AreEqual("Union", method.Parameters[0].Type.Name);
        }

        [Test]
        public void CallableMethodsAcceptLambdas()
        {
            var testGenerator = new TestGenerator
            {
                Files = new()
                {
                    { "Test.cs", @"
using System;

namespace QuantConnect.MethodParserTests
{
    public class TestClass
    {
        public void TestMethod(Action<string> handler)
        {
        }
    }
}" }
            }
            };

            var result = testGenerator.GenerateModelsPublic();

            var namespaces = result.GetNamespaces().ToList();
            Assert.AreEqual(2, namespaces.Count);

            var baseNameSpace = namespaces.Single(x => x.Name == "QuantConnect");
            var testNameSpace = namespaces.Single(x => x.Name == "QuantConnect.MethodParserTests");
            var testClass = testNameSpace.GetClasses().Single();

            var method = testClass.Methods.Single();

            Assert.AreEqual("TestMethod", method.Name);

            Assert.AreEqual(1, method.Parameters.Count);
            var parameter = method.Parameters[0];
            Assert.AreEqual("Callable", parameter.Type.Name);
            Assert.AreEqual("typing", parameter.Type.Namespace);

            Assert.AreEqual(2, parameter.Type.TypeParameters.Count);
            Assert.AreEqual("str", parameter.Type.TypeParameters[0].Name);
            Assert.IsNull(parameter.Type.TypeParameters[0].Namespace);
            Assert.AreEqual("Any", parameter.Type.TypeParameters[1].Name);
            Assert.AreEqual("typing", parameter.Type.TypeParameters[1].Namespace);
        }

        private static IEnumerable<TestCaseData> GetPythonnetTypesTestCases
        {
            get
            {
                yield return new TestCaseData("PyObject", PythonType.Any);
                yield return new TestCaseData("PyList", new PythonType("List", "typing") { TypeParameters = [PythonType.Any] });
                yield return new TestCaseData("PyDict", new PythonType("Dict", "typing") { TypeParameters = new List<PythonType>{ PythonType.Any, PythonType.Any } });
            }
        }

        [TestCaseSource(nameof(GetPythonnetTypesTestCases))]
        public void PythonnetTypeParametersAreConvertedToTypingAny(string pythonnetType, PythonType expectedConvertedType)
        {
            var testGenerator = new TestGenerator
            {
                Files = new()
                {
                    { "Test.cs", @$"
using System;
using System.Collections.Generic;

namespace QuantConnect.MethodParserTests
{{
    public class TestClass
    {{
        public void TestMethod1({pythonnetType} arg)
        {{
        }}
        public void TestMethod2(List<{pythonnetType}> arg)
        {{
        }}
        public void TestMethod3(params {pythonnetType}[] args)
        {{
        }}
        public {pythonnetType} TestMethod4()
        {{
        }}
    }}
}}" }
                }
            };

            var result = testGenerator.GenerateModelsPublic();
            var namespaces = result.GetNamespaces().ToList();

            var baseNameSpace = namespaces.Single(x => x.Name == "QuantConnect");
            var testNameSpace = namespaces.Single(x => x.Name == "QuantConnect.MethodParserTests");
            var testClass = testNameSpace.GetClasses().Single();

            var method1 = testClass.Methods.Single(x => x.Name == "TestMethod1");
            Assert.AreEqual(1, method1.Parameters.Count);
            Assert.AreEqual(expectedConvertedType, method1.Parameters[0].Type);

            var method2 = testClass.Methods.Single(x => x.Name == "TestMethod2");
            Assert.AreEqual(1, method2.Parameters.Count);
            Assert.AreEqual(new PythonType("List", "typing") { TypeParameters = [expectedConvertedType] }, method2.Parameters[0].Type);

            var method3 = testClass.Methods.Single(x => x.Name == "TestMethod3");
            Assert.AreEqual(1, method3.Parameters.Count);
            Assert.AreEqual(new PythonType("Union", "typing") { TypeParameters = [expectedConvertedType, new PythonType("Iterable", "typing") { TypeParameters = [expectedConvertedType] }] }, method3.Parameters[0].Type);
            Assert.IsTrue(method3.Parameters[0].VarArgs);

            var method4 = testClass.Methods.Single(x => x.Name == "TestMethod4");
            Assert.AreEqual(expectedConvertedType, method4.ReturnType);
        }

        [Test]
        public void KeepsCSharpOverloadWhenPythonPartialSharesSignature()
        {
            // Reproduces the QCAlgorithm.Link / BroadcastCommand regression:
            // both partial files collapse to the same Python signature, and when the
            // PyObject-taking partial is visited first, PostProcessClass was deleting the
            // survivor because the only entry in the HashSet was the PyObject variant.
            var testGenerator = new TestGenerator
            {
                Files = new()
                {
                    { "TestClass.Python.cs", @"
using Python.Runtime;

namespace QuantConnect.MethodParserTests
{
    public partial class TestClass
    {
        public string Link(PyObject command) { return null; }
    }
}" },
                    { "TestClass.cs", @"
namespace QuantConnect.MethodParserTests
{
    public partial class TestClass
    {
        public string Link(object command) { return null; }
    }
}" }
                }
            };

            var result = testGenerator.GenerateModelsPublic();

            var testNameSpace = result.GetNamespaces().Single(x => x.Name == "QuantConnect.MethodParserTests");
            var testClass = testNameSpace.GetClasses().Single(x => x.Type.Name == "TestClass");

            var linkMethod = testClass.Methods.SingleOrDefault(x => x.Name == "Link");
            Assert.IsNotNull(linkMethod, "Link should be kept when the C# partial provides it alongside a PyObject overload");
            Assert.IsFalse(linkMethod.HasPyObjectParameter,
                "The surviving Link should come from the C# partial so PostProcessClass does not remove it");
            Assert.AreEqual(1, linkMethod.Parameters.Count);
        }

        [Test]
        public void IndicatorBaseParametersAcceptPythonIndicator()
        {
            var testGenerator = new TestGenerator
            {
                Files = new()
                {
                    { "Test.cs", @"
namespace QuantConnect.Indicators
{
    public class IndicatorDataPoint { }

    public class IndicatorBase<T> { }

    public class TestClass
    {
        public void TestMethod(string symbol, IndicatorBase<IndicatorDataPoint> indicator)
        {
        }
    }
}" }
            }
            };

            var result = testGenerator.GenerateModelsPublic();

            var ns = result.GetNamespaces().Single(x => x.Name == "QuantConnect.Indicators");
            var testClass = ns.GetClasses().Single(x => x.Type.Name == "TestClass");

            var method = testClass.Methods.Single(x => x.Name == "TestMethod");
            var indicatorParam = method.Parameters[1];

            // Should be Union[IndicatorBase[IndicatorDataPoint], PythonIndicator]
            Assert.AreEqual("Union", indicatorParam.Type.Name);
            Assert.AreEqual("typing", indicatorParam.Type.Namespace);
            Assert.AreEqual(2, indicatorParam.Type.TypeParameters.Count);

            var indicatorBaseType = indicatorParam.Type.TypeParameters[0];
            Assert.AreEqual("IndicatorBase", indicatorBaseType.Name);
            Assert.AreEqual("IndicatorDataPoint", indicatorBaseType.TypeParameters[0].Name);

            var pythonIndicatorType = indicatorParam.Type.TypeParameters[1];
            Assert.AreEqual("PythonIndicator", pythonIndicatorType.Name);
            Assert.AreEqual("QuantConnect.Indicators", pythonIndicatorType.Namespace);
        }
    }
}

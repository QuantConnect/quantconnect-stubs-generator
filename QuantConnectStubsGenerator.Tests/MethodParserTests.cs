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

using System.Linq;
using NUnit.Framework;
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
    }
}

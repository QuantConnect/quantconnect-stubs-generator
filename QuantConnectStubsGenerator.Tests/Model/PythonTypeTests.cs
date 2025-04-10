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

using NUnit.Framework;
using QuantConnectStubsGenerator.Model;

namespace QuantConnectStubsGenerator.Tests.Model
{
    [TestFixture]
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

            Assert.AreEqual("typing.Any", type.ToPythonString(true));
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
        public void ToPythonStringCorrectlyAddsNamespace()
        {
            var type = new PythonType("MyClass", "QuantConnect");

            Assert.AreEqual("QuantConnect.MyClass", type.ToPythonString());
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


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

using System;
using System.Linq;
using NUnit.Framework;
using QuantConnectStubsGenerator.Model;

namespace QuantConnectStubsGenerator.Tests.Model
{
    [TestFixture]
    public class ParseContextTests
    {
        [Test]
        public void GetNamespacesShouldReturnAllRegisteredNamespaces()
        {
            var context = new ParseContext();

            var ns1 = new Namespace("ns1");
            var ns2 = new Namespace("ns2");

            context.RegisterNamespace(ns1);
            context.RegisterNamespace(ns2);

            var namespaces = context.GetNamespaces().ToList();

            Assert.AreEqual(2, namespaces.Count);
            Assert.IsTrue(namespaces.Contains(ns1));
            Assert.IsTrue(namespaces.Contains(ns2));
        }

        [Test]
        public void GetNamespaceByNameShouldReturnNamespaceIfItHasBeenRegistered()
        {
            var context = new ParseContext();
            var ns = new Namespace("Test");

            context.RegisterNamespace(ns);

            Assert.AreEqual(ns, context.GetNamespaceByName(ns.Name));
        }

        [Test]
        public void GetNamespaceByNameShouldThrowIfNamespaceHasNotBeenRegistered()
        {
            var context = new ParseContext();

            Assert.Throws<ArgumentException>(() => context.GetNamespaceByName("Test"));
        }

        [Test]
        public void HasNamespaceShouldReturnTrueIfNamespaceHasBeenRegistered()
        {
            var context = new ParseContext();
            var ns = new Namespace("Test");
            context.RegisterNamespace(ns);

            Assert.IsTrue(context.HasNamespace(ns.Name));
        }

        [Test]
        public void HasNamespaceShouldReturnFalseIfNamespaceHasNotBeenRegistered()
        {
            var context = new ParseContext();

            Assert.IsFalse(context.HasNamespace("Test"));
        }
    }
}


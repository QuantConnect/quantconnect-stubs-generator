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

using System.Linq;
using NUnit.Framework;
using QuantConnectStubsGenerator.Model;
using QuantConnectStubsGenerator.Utility;

namespace QuantConnectStubsGenerator.Tests.Utility
{
    [TestFixture]
    public class DependencyGraphTests
    {
        [Test]
        public void GetClassesInOrderShouldReturnTheRegisteredClassesInSuchOrderToMinimizeForwardReferences()
        {
            var classA = new Class(new PythonType("A"));
            var classB = new Class(new PythonType("B"));
            var classC = new Class(new PythonType("C"));

            var dependencyGraph = new DependencyGraph();

            dependencyGraph.AddClass(classA);
            dependencyGraph.AddClass(classB);
            dependencyGraph.AddClass(classC);

            dependencyGraph.AddDependency(classA, classB.Type);
            dependencyGraph.AddDependency(classA, classC.Type);
            dependencyGraph.AddDependency(classB, classC.Type);

            var classes = dependencyGraph.GetClassesInOrder().ToList();

            Assert.AreEqual(3, classes.Count);

            Assert.AreEqual(classC, classes[0]);
            Assert.AreEqual(classB, classes[1]);
            Assert.AreEqual(classA, classes[2]);
        }
    }
}


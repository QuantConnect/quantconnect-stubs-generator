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

        private class TestGenerator : Generator
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

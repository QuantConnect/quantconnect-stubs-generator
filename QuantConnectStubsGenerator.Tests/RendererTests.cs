using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using NUnit.Framework;
using QuantConnectStubsGenerator.Model;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace QuantConnectStubsGenerator.Tests
{
    [TestFixture]
    public class RendererTests
    {
        [Test]
        public void SkipsPropertyIfThereIsAMethodWithTheSameName()
        {
            var testGenerator = new TestGenerator
            {
                Files = new()
                {
                    {
                        "Test1.cs",
                        @"
namespace QuantConnect.Namespace1
{
    public interface IInterface
    {
        string test();
    }

    public class BaseClass : IInterface
    {
        public string test()
        {
            return ""Test"";
        }
    }
}"
                    },
                    {
                        "Test2.cs",
                        @"
using QuantConnect.Namespace1;

namespace QuantConnect.Namespace2
{
    public interface IInterface
    {
        int test2();
    }

    public class TestClass : BaseClass, IInterface
    {
        public int Test { get; set; }

        public int test2()
        {
            return 0;
        }
    }
}"
                    }
                }
            };

            var expectedGeneratedFiles = new[]
            {
                @"
from typing import overload
from enum import Enum
import abc

import QuantConnect.Namespace1
import System

class IInterface(metaclass=abc.ABCMeta):
    """"""This class has no documentation.""""""

    def test(self) -> str:
        ...

class BaseClass(System.Object, QuantConnect.Namespace1.IInterface):
    """"""This class has no documentation.""""""

    def test(self) -> str:
        ...
",
                @"
from typing import overload
from enum import Enum
import abc

import QuantConnect.Namespace1
import QuantConnect.Namespace2

class IInterface(metaclass=abc.ABCMeta):
    """"""This class has no documentation.""""""

    def test_2(self) -> int:
        ...

class TestClass(QuantConnect.Namespace1.BaseClass, QuantConnect.Namespace2.IInterface):
    """"""This class has no documentation.""""""

    def test_2(self) -> int:
        ...
"
            };

            testGenerator.GenerateModelsAndRender(out var context, out var renderedNamespaces);

            var parsedNamespaces = context.GetNamespaces().ToList();
            // QuantConnect, Namespace1, Namespace2 namespaces
            Assert.AreEqual(3, parsedNamespaces.Count);
            // QuantConnect namespace is empty
            Assert.AreEqual(parsedNamespaces.Count - 1, renderedNamespaces.Count);
            Assert.AreEqual(expectedGeneratedFiles.Length, renderedNamespaces.Count);

            for (var i = 0; i < expectedGeneratedFiles.Length; i++)
            {
                var expectedFile = expectedGeneratedFiles[i];
                var renderedFile = renderedNamespaces[i];
                // Remove all whitespace and new lines
                var expectedFileWithoutWhitespace = string.Concat(expectedFile.Where(c => !char.IsWhiteSpace(c)));
                var renderedFileWithoutWhitespace = string.Concat(renderedFile.Where(c => !char.IsWhiteSpace(c)));
                Assert.AreEqual(expectedFileWithoutWhitespace, renderedFileWithoutWhitespace);
            }
        }

        private class TestGenerator : Generator
        {
            private List<StringBuilder> _stringBuilders = new();

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

            protected override TextWriter CreateWriter(string path)
            {
                var stringBuilder = new StringBuilder();
                _stringBuilders.Add(stringBuilder);
                return new StringWriter(stringBuilder);
            }

            public void GenerateModelsAndRender(out ParseContext context, out List<string> renderedNamespaces)
            {
                context = new ParseContext();
                base.GenerateModels(context);

                _stringBuilders.Clear();
                foreach (var ns in context.GetNamespaces())
                {
                    RenderNamespace(ns, "", context);
                }

                renderedNamespaces = _stringBuilders.Select(builder => builder.ToString()).ToList();
            }
        }
    }
}

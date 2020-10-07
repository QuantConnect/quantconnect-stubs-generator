using NUnit.Framework;
using QuantConnectStubsGenerator.Utility;

namespace QuantConnectStubsGenerator.Tests.Utility
{
    [TestFixture, Category("Unit")]
    public class StringExtensionsTests
    {
        [Test]
        public void IndentShouldIndentByFourTimesTheLevelAmountOfSpaces()
        {
            Assert.AreEqual("        # Documentation", "# Documentation".Indent(2));
        }

        [Test]
        public void IndentShouldIndentAllLines()
        {
            Assert.AreEqual("        # Line 1\n        # Line 2", "# Line 1\n# Line 2".Indent(2));
        }
    }
}

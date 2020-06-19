using System.Linq;

namespace QuantConnectStubsGenerator.Utility
{
    public static class StringExtensions
    {
        public static string Indent(this string str, int level = 1)
        {
            var indentation = new string(' ', level * 4);

            var lines = str
                .Split("\n")
                .Select(line => indentation + line);

            return string.Join("\n", lines);
        }
    }
}

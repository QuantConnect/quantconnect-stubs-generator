using System.Collections.Generic;
using System.Linq;

namespace QuantConnectStubsGenerator.Utility
{
    public static class StringExtensions
    {
        private static readonly HashSet<string> _reservedPythonWord = new HashSet<string>()
        {
            "and", "as", "assert", "break", "class", "continue", "def", "del", "elif", "else", "except",
            "False", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", "None",
            "nonlocal", "not", "or", "pass", "raise", "return", "True", "try", "while", "with", "yield"
        };

        public static string Indent(this string str, int level = 1)
        {
            var indentation = new string(' ', level * 4);

            var lines = str
                .Split("\n")
                .Select(line => indentation + line);

            return string.Join("\n", lines);
        }

        public static string ToSnakeCase(this string text, bool constant = false)
        {
            var result = Python.Runtime.Util.ToSnakeCase(text);
            return constant ? result.ToUpperInvariant() : result;
        }

        public static bool IsPythonReservedWord(this string word)
        {
            return _reservedPythonWord.Contains(word);
        }
    }
}

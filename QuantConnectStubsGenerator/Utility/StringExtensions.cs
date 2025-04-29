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
            "nonlocal", "not", "or", "pass", "raise", "return", "True", "try", "while", "with", "yield",
            "await"
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


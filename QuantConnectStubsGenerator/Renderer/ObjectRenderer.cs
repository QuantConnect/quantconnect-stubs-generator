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
using System.IO;
using System.Linq;
using QuantConnectStubsGenerator.Model;
using QuantConnectStubsGenerator.Utility;

namespace QuantConnectStubsGenerator.Renderer
{
    public abstract class ObjectRenderer<T> : BaseRenderer
    {
        private readonly int _indentationLevel;

        private readonly string _indentation;
        private bool _isAtLineStart = true;

        protected ParseContext Context { get; }

        protected ObjectRenderer(TextWriter writer, int indentationLevel, ParseContext context) : base(writer)
        {
            _indentationLevel = indentationLevel;

            _indentation = new string(' ', indentationLevel * 4);
            Context = context;
        }

        public abstract void Render(T item);

        protected override void Write(string value)
        {
            base.Write(IndentIfNecessary(value));
            _isAtLineStart = value.EndsWith("\n");
        }

        protected override void WriteLine(string value = "")
        {
            base.WriteLine(IndentIfNecessary(value).TrimEnd());
            _isAtLineStart = true;
        }

        protected void WriteSummary(string summary, bool indented = false)
        {
            if (summary == null)
            {
                return;
            }

            if (!summary.Contains("\n") && summary.EndsWith("\""))
            {
                summary = summary.Substring(0, summary.Length - 1) + "\\\"";
            }

            var newline = summary.Contains("\n") ? "\n" : "";
            var docstring = $"\"\"\"{newline}{summary}{newline}\"\"\"";

            WriteLine(docstring.Indent(indented ? 1 : 0));
        }

        protected TRenderer CreateRenderer<TRenderer>(bool indented = true)
        {
            var indentationLevel = _indentationLevel + (indented ? 1 : 0);
            return (TRenderer) Activator.CreateInstance(typeof(TRenderer), Writer, indentationLevel, Context);
        }

        private string IndentIfNecessary(string value)
        {
            if (!_isAtLineStart)
            {
                return value;
            }

            var lines = value
                .Split("\n")
                .Select(line => _indentation + line);

            return string.Join("\n", lines);
        }
    }
}


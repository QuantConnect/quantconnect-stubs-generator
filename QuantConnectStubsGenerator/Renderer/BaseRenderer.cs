using System;
using System.IO;
using System.Linq;
using QuantConnectStubsGenerator.Model;
using QuantConnectStubsGenerator.Utility;

namespace QuantConnectStubsGenerator.Renderer
{
    public abstract class BaseRenderer<T>
    {
        private readonly StreamWriter _writer;
        private readonly int _indentationLevel;

        private readonly string _indentation;
        private bool _isAtLineStart = true;

        protected readonly Namespace CurrentNamespace;

        protected BaseRenderer(StreamWriter writer, int indentationLevel, Namespace ns)
        {
            _writer = writer;
            _indentationLevel = indentationLevel;

            CurrentNamespace = ns;

            _indentation = new string(' ', indentationLevel * 4);
        }

        public abstract void Render(T item);

        protected void WriteSummary(string summary, bool indented = false)
        {
            if (summary == null)
            {
                return;
            }

            var summarySuffix = summary.Contains("\n") ? "\n" : "";
            var docstring = $"\"\"\"{summary}{summarySuffix}\"\"\"";

            WriteLine(docstring.Indent(indented ? 1 : 0));
        }

        protected TRenderer CreateRenderer<TRenderer>(bool indented = true)
        {
            var indentationLevel = _indentationLevel + (indented ? 1 : 0);
            return (TRenderer) Activator.CreateInstance(typeof(TRenderer), _writer, indentationLevel, CurrentNamespace);
        }

        protected void Write(string value)
        {
            if (value.Trim() == "")
            {
                value = "";
            }

            _writer.Write(IndentIfNecessary(value));
            _isAtLineStart = value.EndsWith("\n");
        }

        protected void WriteLine(string value = "")
        {
            if (value.Trim() == "")
            {
                value = "";
            }

            _writer.WriteLine(IndentIfNecessary(value).TrimEnd());
            _isAtLineStart = true;
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

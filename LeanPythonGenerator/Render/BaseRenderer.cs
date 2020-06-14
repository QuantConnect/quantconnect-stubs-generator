using System.IO;
using System.Linq;

namespace LeanPythonGenerator.Render
{
    public abstract class BaseRenderer<T>
    {
        protected readonly StreamWriter _writer;
        protected readonly int _indentationLevel;

        private readonly string _indentation;
        private bool _isAtLineStart = true;

        protected BaseRenderer(StreamWriter writer, int indentationLevel)
        {
            _writer = writer;
            _indentationLevel = indentationLevel;
            _indentation = new string(' ', indentationLevel * 4);
        }

        public abstract void Render(T item);

        protected void Write(string value)
        {
            _writer.Write(IndentIfNecessary(value));
            _isAtLineStart = value.EndsWith("\n");
        }

        protected void WriteLine(string value = "")
        {
            _writer.WriteLine(IndentIfNecessary(value));
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

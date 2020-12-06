using System.IO;

namespace QuantConnectStubsGenerator.Renderer
{
    public abstract class BaseRenderer
    {
        protected readonly StreamWriter Writer;

        protected BaseRenderer(StreamWriter writer)
        {
            Writer = writer;
        }

        protected virtual void Write(string value)
        {
            Writer.Write(value);
        }

        protected virtual void WriteLine(string value = "")
        {
            Writer.WriteLine(value);
        }
    }
}

using System.IO;

namespace QuantConnectStubsGenerator.Renderer
{
    public class AlgorithmImportsRenderer : BaseRenderer
    {
        private readonly string _leanPath;

        public AlgorithmImportsRenderer(TextWriter writer, string leanPath) : base(writer)
        {
            _leanPath = leanPath;
        }

        public void Render()
        {
            var algorithmImports = Path.GetFullPath("Common/AlgorithmImports.py", _leanPath);
            WriteLine(File.ReadAllText(algorithmImports));
        }
    }
}

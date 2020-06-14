using System;
using System.IO;
using System.Linq;
using Microsoft.CodeAnalysis.CSharp;

namespace LeanPythonGenerator
{
    class Program
    {
        private string _leanPath;

        private Program(string leanPath)
        {
            _leanPath = leanPath.Replace('\\', '/');

            if (_leanPath.EndsWith("/"))
            {
                _leanPath = _leanPath.Substring(0, _leanPath.Length - 1);
            }
        }

        private void Run()
        {
            // Projects not to generate type hints for
            var blacklistedProjects = new[]
            {
                // Example projects
                "Algorithm.CSharp",
                "Algorithm.FSharp",
                "Algorithm.Python",
                "Algorithm.VisualBasic",

                // Other non-relevant projects
                "PythonToolbox",
                "Tests",
                "Toolbox"
            };

            // Path prefixes for all blacklistedProjects
            var blacklistedPrefixes = blacklistedProjects
                .Select(project => $"{_leanPath}/{project}/");

            // Find all C# files in non-blacklisted projects
            var sourceFiles = Directory
                .EnumerateFiles(_leanPath, "*.cs", SearchOption.AllDirectories)
                .Where(file => !blacklistedPrefixes.Any(file.StartsWith))
                .ToList();

            Console.WriteLine($"Parsing {sourceFiles.Count} C# files");

            // Create syntax trees for all C# files
            var syntaxTrees = sourceFiles
                .Select(file => CSharpSyntaxTree.ParseText(File.ReadAllText(file)))
                .ToList();

            // Create a compilation containing all syntax trees to retrieve semantic models containing type info from
            var compilation = CSharpCompilation.Create("").AddSyntaxTrees(syntaxTrees);
        }

        static void Main(string[] args)
        {
            if (args.Length != 1)
            {
                Console.WriteLine("Usage: dotnet run <path to Lean>");
                Environment.Exit(1);
            }

            new Program(args[0]).Run();
        }
    }
}

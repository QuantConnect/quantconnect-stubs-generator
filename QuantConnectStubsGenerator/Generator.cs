using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using log4net;
using log4net.Config;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using QuantConnectStubsGenerator.Model;
using QuantConnectStubsGenerator.Parser;
using QuantConnectStubsGenerator.Renderer;

namespace QuantConnectStubsGenerator
{
    public class Generator
    {
        private static readonly ILog Logger = LogManager.GetLogger(typeof(Generator));

        private readonly string _leanPath;
        private readonly string _outputDirectory;

        public Generator(string leanPath, string outputDirectory)
        {
            _leanPath = FormatPath(leanPath);
            _outputDirectory = FormatPath(outputDirectory);
        }

        public void Run()
        {
            // Projects not to generate stubs for
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
                "ToolBox"
            };

            // Path prefixes for all blacklistedProjects
            var blacklistedPrefixes = blacklistedProjects
                .Select(project => $"{_leanPath}/{project}")
                .ToList();

            // Find all C# files in non-blacklisted projects
            var sourceFiles = Directory
                .EnumerateFiles(_leanPath, "*.cs", SearchOption.AllDirectories)
                .Where(file => !blacklistedPrefixes.Any(file.StartsWith))
                .ToList();

            Logger.Info($"Parsing {sourceFiles.Count} C# files");

            // Create syntax trees for all C# files
            var syntaxTrees = sourceFiles
                .Select(file => CSharpSyntaxTree.ParseText(File.ReadAllText(file), path: file))
                .ToList();

            // Create a compilation containing all syntax trees to retrieve semantic models from
            var compilation = CSharpCompilation.Create("").AddSyntaxTrees(syntaxTrees);

            // Add all assemblies in current project to compilation to improve semantic models
            foreach (var assembly in AppDomain.CurrentDomain.GetAssemblies())
            {
                if (!assembly.IsDynamic && assembly.Location != "")
                {
                    compilation = compilation.AddReferences(MetadataReference.CreateFromFile(assembly.Location));
                }
            }

            // Create an empty ParseContext which will be filled with all relevant information during parsing
            var context = new ParseContext();

            // Parse all syntax trees using all parsers
            ParseSyntaxTrees<ClassParser>(context, syntaxTrees, compilation);
            ParseSyntaxTrees<PropertyParser>(context, syntaxTrees, compilation);
            ParseSyntaxTrees<MethodParser>(context, syntaxTrees, compilation);

            // Render .pyi files containing stubs for all parsed namespaces
            foreach (var ns in context.GetNamespaces())
            {
                RenderNamespace(ns);
            }
        }

        private void ParseSyntaxTrees<T>(
            ParseContext context,
            IEnumerable<SyntaxTree> syntaxTrees,
            CSharpCompilation compilation) where T : BaseParser
        {
            foreach (var tree in syntaxTrees)
            {
                Logger.Debug($"Running {typeof(T).Name} on {tree.FilePath}");

                var model = compilation.GetSemanticModel(tree);
                var parser = (T) Activator.CreateInstance(typeof(T), context, model);

                if (parser == null)
                {
                    throw new SystemException($"Could not create {typeof(T).Name} for {tree.FilePath}");
                }

                parser.Visit(tree.GetRoot());
            }
        }

        private void RenderNamespace(Namespace ns)
        {
            var namespacePath = ns.Name.Replace('.', '/');
            var outputPath = Path.GetFullPath($"{namespacePath}/__init__.py", _outputDirectory);

            // QuantConnect.API stubs are placed in QuantConnect/API/__init__.py
            // QuantConnect.Api stubs are placed in QuantConnect/Api.py
            // This is done to prevent case-sensitivity issues
            if (ns.Name == "QuantConnect.Api")
            {
                outputPath = Path.GetFullPath($"{namespacePath}.py", _outputDirectory);
            }

            Logger.Info($"Generating {outputPath}");

            // Make sure the parent directories of outputPath exist
            new FileInfo(outputPath).Directory?.Create();

            using var pyiWriter = new StreamWriter(outputPath);
            var renderer = new NamespaceRenderer(pyiWriter, 0, ns);
            renderer.Render(ns);
        }

        private string FormatPath(string path)
        {
            var cwd = Directory.GetCurrentDirectory();
            var resolvedPath = Path.GetFullPath(path, cwd);

            var normalizedPath = resolvedPath.Replace('\\', '/');

            return normalizedPath.EndsWith("/")
                ? normalizedPath.Substring(0, path.Length - 1)
                : normalizedPath;
        }
    }
}

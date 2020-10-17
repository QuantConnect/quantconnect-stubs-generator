using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using log4net;
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

            // Ensure all directories contain a __init__.py file so import resolutions work properly
            EnsureAllModulesReachable();

            // Render setup.py file supporting local installation
            GenerateSetup();
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
            var outputPath = Path.GetFullPath($"{namespacePath}/__init__.pyi", _outputDirectory);

            // QuantConnect.API stubs are placed in QuantConnect/API/__init__.pyi
            // QuantConnect.Api stubs are placed in QuantConnect/Api.pyi
            // This is done to prevent case-sensitivity issues
            if (ns.Name == "QuantConnect.Api")
            {
                outputPath = Path.GetFullPath($"{namespacePath}.pyi", _outputDirectory);
            }

            Logger.Info($"Generating {outputPath}");

            // Make sure the parent directories of outputPath exist
            new FileInfo(outputPath).Directory?.Create();

            using var pyiWriter = new StreamWriter(outputPath);
            var renderer = new NamespaceRenderer(pyiWriter, 0);
            renderer.Render(ns);
        }

        private void EnsureAllModulesReachable()
        {
            var oandaDirectories =
                new DirectoryInfo(Path.GetFullPath("Oanda", _outputDirectory))
                    .GetDirectories("*.*", SearchOption.AllDirectories);

            var qcDirectories =
                new DirectoryInfo(Path.GetFullPath("QuantConnect", _outputDirectory))
                    .GetDirectories("*.*", SearchOption.AllDirectories);

            foreach (var directory in oandaDirectories.Concat(qcDirectories))
            {
                var initPath = Path.GetFullPath("__init__.pyi", directory.FullName);

                if (new FileInfo(initPath).Exists)
                {
                    continue;
                }

                Logger.Info($"Generating empty {initPath}");

                using var initWriter = new StreamWriter(initPath);
                initWriter.WriteLine("# This namespace is empty");
                initWriter.WriteLine("# This file exists to make import resolution work properly");
            }
        }

        private void GenerateSetup()
        {
            var namespaces = Directory.GetFiles(_outputDirectory, "*.pyi", SearchOption.AllDirectories)
                .Select(file =>
                {
                    var ns = file.Replace(_outputDirectory, "").Substring(1);
                    ns = ns.Substring(0, ns.LastIndexOf('/'));
                    return ns.Replace('/', '.');
                }).Distinct().OrderBy(name => name).ToList();

            var setupPath = Path.GetFullPath("setup.py", _outputDirectory);
            using var setupWriter = new StreamWriter(setupPath);

            Logger.Info($"Generating {setupPath}");

            setupWriter.WriteLine("from setuptools import setup");
            setupWriter.WriteLine();
            setupWriter.WriteLine("setup(");
            setupWriter.WriteLine("    name='quantconnect-stubs',");
            setupWriter.WriteLine($"    version='{GetLatestTag()}',");
            setupWriter.WriteLine("    description='Unofficial stubs for QuantConnect\\'s Lean',");
            setupWriter.WriteLine("    python_requires='>=3.6',");
            setupWriter.WriteLine("    packages=[");

            foreach (var ns in namespaces)
            {
                setupWriter.WriteLine($"        '{ns}',");
            }

            setupWriter.WriteLine("    ],");
            setupWriter.WriteLine("    package_data={");

            foreach (var ns in namespaces)
            {
                setupWriter.WriteLine($"        '{ns}': ['*.pyi'],");
            }

            setupWriter.WriteLine("    }");
            setupWriter.WriteLine(")");
        }

        private int GetLatestTag()
        {
            var tagsDirectory = new DirectoryInfo(Path.GetFullPath(".git/refs/tags", _leanPath));

            if (!tagsDirectory.Exists)
            {
                throw new Exception("Provided Lean path is not a Git repository");
            }

            var files = tagsDirectory
                .GetFiles()
                .Select(file => file.Name)
                .Select(name => int.TryParse(name, out int n) ? n : (int?) null)
                .Where(tag => tag.HasValue)
                .Select(tag => tag.Value)
                .OrderBy(tag => tag)
                .ToList();

            if (files.Count == 0)
            {
                throw new Exception("Provided Lean path is not a Git repository with tags");
            }

            return files.Last();
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

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

            // Create empty namespaces to fill gaps in between namespaces like "A.B" and "A.B.C.D"
            // This is needed to make import resolution work correctly
            CreateEmptyNamespaces(context);

            // Render .pyi files containing stubs for all parsed namespaces
            foreach (var ns in context.GetNamespaces())
            {
                RenderNamespace(context, ns);
            }

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

        private void CreateEmptyNamespaces(ParseContext context)
        {
            // The key is the namespace, the value is whether there is already a namespace for it
            // After adding all namespaces, the keys of entries with a false value represent the gap namespaces
            var namespaceMapping = new Dictionary<string, bool>();

            foreach (var ns in context.GetNamespaces())
            {
                namespaceMapping[ns.Name] = true;

                var parts = ns.Name.Split(".");

                for (var i = 1; i <= parts.Length; i++)
                {
                    var partialNamespace = string.Join(".", parts.Take(i));

                    if (!namespaceMapping.ContainsKey(partialNamespace))
                    {
                        namespaceMapping[partialNamespace] = false;
                    }
                }
            }

            foreach (var (ns, exists) in namespaceMapping)
            {
                if (!exists)
                {
                    context.RegisterNamespace(new Namespace(ns));
                }
            }
        }

        private void RenderNamespace(ParseContext context, Namespace ns)
        {
            var namespacePath = ns.Name.Replace('.', '/');
            var outputPath = Path.GetFullPath($"{namespacePath}/__init__.pyi", _outputDirectory);

            Logger.Info($"Generating {outputPath}");

            // Make sure the parent directories of outputPath exist
            new FileInfo(outputPath).Directory?.Create();

            using var writer = new StreamWriter(outputPath);
            var renderer = new NamespaceRenderer(writer, 0);
            renderer.Render(ns);

            CreatePyLoader(context, ns.Name, outputPath.Replace(".pyi", ".py"));
        }

        private void CreatePyLoader(ParseContext context, string ns, string path)
        {
            Logger.Info($"Generating {path}");

            using var writer = new StreamWriter(path);
            var namespaceRoots = context
                .GetNamespaces()
                .Select(n => n.Name.Split(".")[0])
                .Distinct()
                .OrderBy(n => n)
                .ToList();

            writer.WriteLine($@"
# pyright: reportMissingImports=false

import os
import sys

# Lean uses Python.NET to support importing C# code in Python code.
#
# If quantconnect-stubs is installed via pip and Lean is ran locally,
# importing anything from the QuantConnect namespace makes the Python
# interpreter look in the quantconnect-stubs package for the implementation.
#
# The desired behavior is for the interpreter to use the implementation
# provided by the AddReference() call from Python.NET.
#
# To fix this, we temporarily remove the directory containing the
# quantconnect-stubs package from sys.path and re-import the current namespace
# so the relevant C# namespace is used when running Lean locally.

# Find the directory containing quantconnect-stubs (usually site-packages)
current_path = os.path.dirname(__file__)
while os.path.basename(current_path) not in [{string.Join(", ", namespaceRoots.Select(n => $"'{n}'"))}]:
    current_path = os.path.dirname(current_path)
current_path = os.path.dirname(current_path)

# Temporarily remove the directory containing quantconnect-stubs from sys.path
original_path = sys.path[:]
sys.path.remove(current_path)

# Import the C# version of the current namespace
del sys.modules['{ns}']
from clr import AddReference
AddReference('{ns}')
from {ns} import *

# Restore sys.path
sys.path = original_path
            ".Trim());
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
            using var writer = new StreamWriter(setupPath);

            Logger.Info($"Generating {setupPath}");

            writer.WriteLine($@"
from setuptools import setup

long_description = '''
# QuantConnect Stubs

This package contains type stubs for QuantConnect's Lean.

See the [repository](https://github.com/QuantConnect/quantconnect-stubs-generator) for more information.

## Installation

```
pip install quantconnect-stubs
```
'''.strip()

setup(
    name='quantconnect-stubs',
    version='{GetVersion()}',
    description='Type stubs for QuantConnect\'s Lean',
    author='QuantConnect',
    author_email='support@quantconnect.com',
    url='https://github.com/QuantConnect/quantconnect-stubs-generator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3'
    ],
    packages=[
{string.Join(",\n", namespaces.Select(ns => new string(' ', 8) + $"'{ns}'"))}
    ],
    package_data={{
{string.Join(",\n", namespaces.Select(ns => new string(' ', 8) + $"'{ns}': ['*.py', '*.pyi']"))}
    }}
)
            ".Trim());
        }

        private string GetVersion()
        {
            const string defaultVersion = "1.0.0";
            var tagsDirectory = new DirectoryInfo(Path.GetFullPath(".git/refs/tags", _leanPath));

            if (!tagsDirectory.Exists)
            {
                Logger.Warn($"Provided Lean path is not a Git repository, setting version to {defaultVersion}");
                return defaultVersion;
            }

            var files = tagsDirectory
                .GetFiles()
                .Select(file => file.Name)
                .Select(name => int.TryParse(name, out var n) ? n : (int?) null)
                .Where(tag => tag.HasValue)
                .Select(tag => tag.Value)
                .OrderBy(tag => tag)
                .ToList();

            if (files.Count != 0)
            {
                return files.Last().ToString();
            }

            Logger.Warn($"Provided Lean path is not a Git repository with tags, setting version to {defaultVersion}");
            return defaultVersion;
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

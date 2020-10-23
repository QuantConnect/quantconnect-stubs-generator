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
        private readonly string _runtimePath;
        private readonly string _outputDirectory;

        public Generator(string leanPath, string runtimePath, string outputDirectory)
        {
            _leanPath = FormatPath(leanPath);
            _runtimePath = FormatPath(runtimePath);
            _outputDirectory = FormatPath(outputDirectory);
        }

        public void Run()
        {
            // Lean projects not to generate stubs for
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

            // Path prefixes for all blacklisted projects
            var blacklistedPrefixes = blacklistedProjects
                .Select(project => $"{_leanPath}/{project}")
                .ToList();

            // Find all C# files in non-blacklisted projects in Lean
            var leanFiles = Directory
                .EnumerateFiles(_leanPath, "*.cs", SearchOption.AllDirectories)
                .Where(file => !blacklistedPrefixes.Any(file.StartsWith))
                .ToList();

            // Find all relevant C# files in the C# runtime
            var coreLibPath = Path.GetFullPath("src/libraries/System.Private.CoreLib/src", _runtimePath);
            var monoCoreLibPath = Path.GetFullPath("src/mono/netcore/System.Private.CoreLib/src", _runtimePath);

            var coreLibFiles = Directory
                .EnumerateFiles(coreLibPath, "*.cs", SearchOption.AllDirectories)
                .ToList();

            var monoCoreLibFiles = Directory
                .EnumerateFiles(monoCoreLibPath, "*.Mono.cs", SearchOption.AllDirectories)
                .ToList();

            // Gather all C# files that need to be parsed
            var sourceFiles = leanFiles.Concat(coreLibFiles).Concat(monoCoreLibFiles).ToList();

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
                var namespacePath = ns.Name.Replace('.', '/');
                var basePath = Path.GetFullPath($"{namespacePath}/__init__", _outputDirectory);

                RenderNamespace(ns, basePath + ".pyi");
                GeneratePyLoader(ns.Name, basePath + ".py");
            }

            // Generate stubs for the clr module
            GenerateClrStubs();

            // Create setup.py
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

        private void RenderNamespace(Namespace ns, string outputPath)
        {
            // Don't generate empty .pyi files
            if (!ns.GetParentClasses().Any())
            {
                return;
            }

            Logger.Info($"Generating {outputPath}");

            EnsureParentDirectoriesExist(outputPath);

            using var writer = new StreamWriter(outputPath);
            var renderer = new NamespaceRenderer(writer, 0);
            renderer.Render(ns);
        }

        private void GeneratePyLoader(string ns, string outputPath)
        {
            Logger.Info($"Generating {outputPath}");

            EnsureParentDirectoriesExist(outputPath);

            using var writer = new StreamWriter(outputPath);
            writer.WriteLine($@"
# pyright: reportMissingImports=false

import os
import sys

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
while os.path.basename(current_path) != '{ns.Split(".")[0]}':
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

        private void GenerateClrStubs()
        {
            var outputPath = Path.GetFullPath("clr/__init__.pyi", _outputDirectory);
            Logger.Info($"Generating {outputPath}");

            EnsureParentDirectoriesExist(outputPath);

            using var writer = new StreamWriter(outputPath);
            writer.WriteLine($@"
import typing

import System
import System.Reflection


def getPreload() -> bool:
    ...

def setPreload(preloadFlag: bool) -> None:
    ...

def AddReference(name: str) -> System.Reflection.Assembly:
    ...

def GetClrType(type: typing.Type[typing.Any]) -> System.Type:
    ...

def FindAssembly(name: str) -> str:
    ...

def ListAssemblies(verbose: bool) -> typing.List[System.Reflection.Assembly]:
    ...
            ".Trim());
        }

        private void GenerateSetup()
        {
            var namespaces = Directory.GetFiles(_outputDirectory, "__init__.py*", SearchOption.AllDirectories)
                .Select(file =>
                {
                    var ns = file.Replace(_outputDirectory, "").Substring(1);
                    ns = ns.Substring(0, ns.Contains('/') ? ns.LastIndexOf('/') : ns.Length);
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

        private void EnsureParentDirectoriesExist(string path)
        {
            new FileInfo(path).Directory?.Create();
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

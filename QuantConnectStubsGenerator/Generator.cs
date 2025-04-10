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
using System.Collections.Generic;
using System.Text.RegularExpressions;
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
            // Create an empty ParseContext which will be filled with all relevant information during parsing
            var context = new ParseContext();

            GenerateModels(context);

            // Render .pyi files containing stubs for all parsed namespaces
            Logger.Info($"Generating .py and .pyi files for {context.GetNamespaces().Count()} namespaces");
            foreach (var ns in context.GetNamespaces())
            {
                var namespacePath = ns.Name.Replace('.', '/');
                var basePath = Path.GetFullPath($"{namespacePath}/__init__", _outputDirectory);

                RenderNamespace(ns, basePath + ".pyi", context);
                GeneratePyLoader(ns.Name, basePath + ".py");
                CreateTypedFileForNamespace(ns.Name);
            }

            // Generate stubs for the clr module
            GenerateClrStubs();

            // Generate stubs for https://github.com/QuantConnect/Lean/blob/master/Common/AlgorithmImports.py
            GenerateAlgorithmImports();

            // Create setup.py
            GenerateSetup();
        }

        protected virtual void GenerateModels(ParseContext context)
        {
            // Create syntax trees for all C# files
            var syntaxTrees = GetSyntaxTrees().ToList();

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

            // Parse all syntax trees using all parsers
            ParseSyntaxTrees<ClassParser>(context, syntaxTrees, compilation);
            ParseSyntaxTrees<PropertyParser>(context, syntaxTrees, compilation);
            ParseSyntaxTrees<MethodParser>(context, syntaxTrees, compilation);

            // Perform post-processing on all parsed classes
            foreach (var ns in context.GetNamespaces())
            {

                // Remove problematic method "GetMethodInfo" from System.Reflection.RuntimeReflectionExtensions
                // KW arg is `del` which python is not a fan of. TODO: Make this post filtering more generic?
                if (ns.Name == "System.Reflection")
                {
                    var reflectionClass = ns.GetClasses()
                        .FirstOrDefault(x => x.Type.Name == "RuntimeReflectionExtensions");
                    var badMethod = reflectionClass.Methods.FirstOrDefault(x => x.Name == "GetMethodInfo");

                    reflectionClass.Methods.Remove(badMethod);
                }


                foreach (var cls in ns.GetClasses())
                {
                    // Remove Python implementations for methods where there is both a Python as well as a C# implementation
                    // The parsed C# implementation is usually more useful for autocomplete
                    // To improve it a little bit we move the return type of the Python implementation to the C# implementation
                    PostProcessClass(cls);

                    // Mark methods which appear multiple times as overloaded
                    MarkOverloads(cls);
                }
            }

            // Create empty namespaces to fill gaps in between namespaces like "A.B" and "A.B.C.D"
            // This is needed to make import resolution work correctly
            CreateEmptyNamespaces(context);
        }

        protected virtual IEnumerable<SyntaxTree> GetSyntaxTrees()
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

            // Create our blacklisted regex list, we will skip these files in stubs generation
            // 1. DataSource repos unnecessary projects, algorithms, etc (Under ADDITIONAL_STUBS dir, see ci_build_stubs.sh)
            // 2. Any bin CS files
            List<Regex> blacklistedRegex = new()
            {
                new (".*Lean\\/ADDITIONAL_STUBS\\/.*(?:DataProcessing|tests|DataQueueHandlers|Demonstration|Demostration|Algorithm)",  RegexOptions.Compiled),
                new(".*\\/bin\\/", RegexOptions.Compiled),
            };

            // Path prefixes for all blacklisted projects
            var blacklistedPrefixes = blacklistedProjects
                .Select(project => $"{_leanPath}/{project}")
                .ToList();

            // Find all C# files in non-blacklisted projects in Lean
            var sourceFiles = Directory
                .EnumerateFiles(_leanPath, "*.cs", SearchOption.AllDirectories)
                .Where(file => !blacklistedRegex.Any(regex => regex.IsMatch(file)))
                .Where(file => !blacklistedPrefixes.Any(file.Replace("\\", "/").StartsWith))
                .ToList();

            // Find all relevant C# files in the C# runtime
            foreach (var (relativePath, searchPattern) in new Dictionary<string, string>
            {
                { "src/libraries/System.Private.CoreLib/src", "*.cs" },
                { "src/mono/System.Private.CoreLib/src", "*.Mono.cs" },
                { "src/libraries/System.Drawing.Primitives/src", "*.cs" },
                { "src/libraries/System.Collections/src", "*.cs" },
                { "src/libraries/System.Collections.Immutable/src", "*.cs" },
                { "src/libraries/System.Collections.Concurrent/src", "*.cs" },
                { "src/libraries/System.ObjectModel/src", "*.cs" },
                { "src/libraries/System.ComponentModel.Annotations/src", "*.cs" },
                { "src/libraries/System.ComponentModel.TypeConverter/src", "*.cs" },
                { "src/libraries/System.Net.Primitives/src", "*.cs" },
                { "src/libraries/System.Linq/src", "*.cs" },
                { "src/libraries/System.Console/src", "*.cs" },
                { "src/libraries/System.Text.RegularExpressions/src", "*.cs" }
            })
            {
                var absolutePath = Path.GetFullPath(relativePath, _runtimePath);
                var files = Directory
                    .EnumerateFiles(absolutePath, searchPattern, SearchOption.AllDirectories)
                    .ToList();

                sourceFiles.AddRange(files);
            }

            Logger.Info($"Parsing {sourceFiles.Count} C# files");

            foreach (var file in sourceFiles)
            {
                yield return CSharpSyntaxTree.ParseText(File.ReadAllText(file), path: file);
            }
        }

        /// <summary>
        /// We create an empty 'py.typed' file at the root of our package folders PEP 561
        /// See https://peps.python.org/pep-0561/
        /// </summary>
        private void CreateTypedFileForNamespace(string name)
        {
            var root = name;
            var rootIndex = name.IndexOf('.');
            if (rootIndex != -1)
            {
                root = name.Substring(0, rootIndex);
            }

            var rootPath = Path.GetFullPath($"{root.Replace('.', '/')}/py.typed", _outputDirectory);
            if (!File.Exists(rootPath))
            {
                File.WriteAllText(rootPath, "");
            }
        }

        private void ParseSyntaxTrees<T>(
            ParseContext context,
            IEnumerable<SyntaxTree> syntaxTrees,
            CSharpCompilation compilation) where T : BaseParser
        {
            Logger.Info($"Running {typeof(T).Name} on all syntax trees");

            foreach (var tree in syntaxTrees)
            {
                var model = compilation.GetSemanticModel(tree);
                var parser = (T)Activator.CreateInstance(typeof(T), context, model);

                if (parser == null)
                {
                    throw new SystemException($"Could not create {typeof(T).Name} for {tree.FilePath}");
                }

                try
                {
                    parser.Visit(tree.GetRoot());
                }
                catch (Exception e)
                {
                    throw new Exception($"Generator crashed while running {typeof(T).Name} on {tree.FilePath}", e);
                }
            }
        }

        private void PostProcessClass(Class cls)
        {
            var loggingMethods = new HashSet<string>
            {
                "QCAlgorithm.Debug",
                "QCAlgorithm.Error",
                "QCAlgorithm.Log",
                "QCAlgorithm.Quit"
            };

            var pythonMethodsToRemove = cls.Methods
                .Where(m => m.File != null && m.File.EndsWith(".Python.cs"))
                // Python implementations of logging methods accept any parameter type
                // C# implementations only accept strings/numbers, so we cannot remove the Python implementations
                .Where(m => !loggingMethods.Contains($"{cls.Type.Name}.{m.Name}"))
                // A few C# methods like AddData<T>(...) have a Python implementation like AddData(dataType, ...)
                // We cannot remove the Python implementation here as it contains useful information
                .Where(m =>
                {
                    if (m.Parameters.Count == 0)
                    {
                        return true;
                    }

                    var paramName = m.Parameters[0].Name;
                    return paramName != "type" && paramName != "dataType" && paramName != "T";
                })
                .ToList();

            foreach (var pythonMethod in pythonMethodsToRemove)
            {
                foreach (var otherMethod in cls.Methods.Where(m => m.Name == pythonMethod.Name))
                {
                    otherMethod.ReturnType = pythonMethod.ReturnType;
                }

                cls.Methods.Remove(pythonMethod);
            }
        }

        private void MarkOverloads(Class cls)
        {
            var duplicateMethodNames = cls.Methods
                .GroupBy(m => m.Name)
                .Where(group => group.Count() > 1)
                .Select(group => group.Key);

            foreach (var name in duplicateMethodNames)
            {
                foreach (var method in cls.Methods.Where(m => m.Name == name))
                {
                    method.Overload = true;
                }
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

        protected void RenderNamespace(Namespace ns, string outputPath, ParseContext context)
        {
            // Don't generate empty .pyi files
            if (!ns.GetParentClasses().Any())
            {
                return;
            }

            using var writer = CreateWriter(outputPath);
            var renderer = new NamespaceRenderer(writer, 0, context);
            renderer.Render(ns);
        }

        private void GeneratePyLoader(string ns, string outputPath)
        {
            using var writer = CreateWriter(outputPath);
            var renderer = new PyLoaderRenderer(writer);
            renderer.Render(ns);
        }

        private void GenerateClrStubs()
        {
            Logger.Info("Generating clr stubs");

            var outputPath = Path.GetFullPath("clr/__init__.pyi", _outputDirectory);

            using var writer = CreateWriter(outputPath);
            var renderer = new ClrStubsRenderer(writer);
            renderer.Render();

            CreateTypedFileForNamespace("clr");
        }

        private void GenerateAlgorithmImports()
        {
            Logger.Info("Generating AlgorithmImports stubs");

            var outputPath = Path.GetFullPath("AlgorithmImports/__init__.pyi", _outputDirectory);
            using var writer = CreateWriter(outputPath);
            var renderer = new AlgorithmImportsRenderer(writer, _leanPath);
            renderer.Render();

            CreateTypedFileForNamespace("AlgorithmImports");
        }

        private void GenerateSetup()
        {
            Logger.Info("Generating setup.py");

            var setupPath = Path.GetFullPath("setup.py", _outputDirectory);

            using var writer = CreateWriter(setupPath);
            var renderer = new SetupRenderer(writer, _leanPath, _outputDirectory);
            renderer.Render();
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

        protected virtual TextWriter CreateWriter(string path)
        {
            // Ensure parent directories exist
            new FileInfo(path).Directory?.Create();
            return new StreamWriter(path);
        }
    }
}


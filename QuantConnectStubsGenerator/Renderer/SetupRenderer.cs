using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using log4net;

namespace QuantConnectStubsGenerator.Renderer
{
    public class SetupRenderer : BaseRenderer
    {
        private static readonly ILog Logger = LogManager.GetLogger(typeof(SetupRenderer));

        private readonly string _leanPath;
        private readonly string _outputDirectory;

        public SetupRenderer(StreamWriter writer, string leanPath, string outputDirectory) : base(writer)
        {
            _leanPath = leanPath;
            _outputDirectory = outputDirectory;
        }

        public void Render()
        {
            var packageVersion = GetPackageVersion();
            var namespaces = GetNamespaces();

            var pandasVersion = GetPandasVersion();
            var pandasVersionConstraint = pandasVersion != null ? $">={pandasVersion}" : "";

            WriteLine($@"
from setuptools import setup

long_description = """"""
# QuantConnect Stubs

This package contains type stubs for QuantConnect's [Lean](https://github.com/QuantConnect/Lean) algorithmic trading engine and for parts of the .NET library that are used by Lean.

These stubs can be used by editors to provide type-aware features like autocompletion and auto-imports in QuantConnect strategies written in Python.
"""""".strip()

setup(
    name=""quantconnect-stubs"",
    version=""{packageVersion}"",
    description=""Type stubs for QuantConnect's Lean"",
    author=""QuantConnect"",
    author_email=""support@quantconnect.com"",
    url=""https://github.com/QuantConnect/quantconnect-stubs-generator"",
    long_description=long_description,
    long_description_content_type=""text/markdown"",
    classifiers=[
        ""Development Status :: 5 - Production/Stable"",
        ""Intended Audience :: Developers"",
        ""Intended Audience :: Financial and Insurance Industry"",
        ""License :: OSI Approved :: Apache Software License"",
        ""Programming Language :: Python :: 3""
    ],
    install_requires=[""pandas{pandasVersionConstraint}""],
    packages=[
{string.Join(",\n", namespaces.Select(ns => new string(' ', 8) + $"\"{ns}\""))}
    ],
    package_data={{
{string.Join(",\n", namespaces.Select(ns => new string(' ', 8) + $"\"{ns}\": [\"*.py\", \"*.pyi\"]"))}
    }}
)
            ".Trim());
        }

        private string GetPackageVersion()
        {
            if (Environment.GetEnvironmentVariables().Contains("STUBS_VERSION"))
            {
                return Environment.GetEnvironmentVariables()["STUBS_VERSION"]?.ToString();
            }

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

        private List<string> GetNamespaces()
        {
            return Directory.GetFiles(_outputDirectory, "__init__.py*", SearchOption.AllDirectories)
                .Select(file =>
                {
                    var ns = file.Replace(_outputDirectory, "").Substring(1);
                    ns = ns.Substring(0, ns.Contains('/') ? ns.LastIndexOf('/') : ns.Length);
                    return ns.Replace('/', '.');
                }).Distinct().OrderBy(name => name).ToList();
        }

        private string GetPandasVersion()
        {
            var dockerFilePath = Path.GetFullPath("DockerfileLeanFoundation", _leanPath);
            if (File.Exists(dockerFilePath))
            {
                var dockerFileContents = File.ReadAllText(dockerFilePath);
                var versionMatch = new Regex(@"pandas=(\d+\.\d+\.\d+)").Match(dockerFileContents);

                if (versionMatch.Success)
                {
                    return versionMatch.Groups[1].Value;
                }
            }

            Logger.Warn("Provided Lean path does not contain a Dockerfile pinning pandas to a specific version");
            return null;
        }
    }
}

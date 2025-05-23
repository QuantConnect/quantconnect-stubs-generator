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
using System.IO;
using System.Linq;
using log4net;

namespace QuantConnectStubsGenerator.Renderer
{
    public class SetupRenderer : BaseRenderer
    {
        private static readonly ILog Logger = LogManager.GetLogger(typeof(SetupRenderer));

        private readonly string _leanPath;
        private readonly string _outputDirectory;

        public SetupRenderer(TextWriter writer, string leanPath, string outputDirectory) : base(writer)
        {
            _leanPath = leanPath;
            _outputDirectory = outputDirectory;
        }

        public void Render()
        {
            var packageVersion = GetPackageVersion();
            var namespaces = GetNamespaces();

            WriteLine($@"
from setuptools import setup

long_description = """"""
# QuantConnect Stubs

This package contains type stubs for QuantConnect's [Lean](https://github.com/QuantConnect/Lean) algorithmic trading engine and for parts of the .NET library that are used by Lean.

These stubs can be used by editors to provide type-aware features like autocomplete and auto-imports in QuantConnect strategies written in Python.

After installing the stubs, you can copy the following line to the top of every Python file to have the same imports as the ones that are added by default in the cloud:
```py
from AlgorithmImports import *
```

This line imports [all common QuantConnect members](https://github.com/QuantConnect/Lean/blob/master/Common/AlgorithmImports.py) and provides autocomplete for them.
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
    install_requires=[""pandas"", ""matplotlib""],
    packages=[
{string.Join(",\n", namespaces.Select(ns => new string(' ', 8) + $"\"{ns}\""))}
    ],
    package_data={{
{string.Join(",\n", namespaces.Select(ns => new string(' ', 8) + $"\"{ns}\": [\"*.py\", \"*.pyi\", \"py.typed\"]"))}
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
                .Select(name => int.TryParse(name, out var n) ? n : (int?)null)
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
                .Select(file => file.Replace('\\', '/'))
                .Select(file =>
                {
                    var ns = file.Replace(_outputDirectory, "").Substring(1);
                    ns = ns.Substring(0, ns.Contains('/') ? ns.LastIndexOf('/') : ns.Length);
                    return ns.Replace('/', '.');
                }).Distinct().OrderBy(name => name).ToList();
        }
    }
}

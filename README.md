# QuantConnect Stubs Generator

[![Build Status](https://github.com/QuantConnect/quantconnect-stubs-generator/workflows/Build/badge.svg)](https://github.com/QuantConnect/quantconnect-stubs-generator/actions?query=workflow%3ABuild)
[![PyPI Version](https://img.shields.io/pypi/v/quantconnect-stubs)](https://pypi.org/project/quantconnect-stubs/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/quantconnect-stubs)](https://pypi.org/project/quantconnect-stubs/)

QuantConnect Stubs Generator is a program which generates Python stubs based on the C# files in [QuantConnect/Lean](https://github.com/QuantConnect/Lean) and [dotnet/runtime](https://github.com/dotnet/runtime). These stubs can be used by editors to provide type-aware features like autocompletion and auto-imports in QuantConnect strategies written in Python.

## Installation

The latest version of the stubs can be installed by running `pip install -U quantconnect-stubs`. Every time Lean is updated, a new version of the package is released containing the latest stubs (the same command can be used to update).

The stubs are tested to work well with PyCharm and VS Code in combination with the [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) extension. They should also work with any other editor capable of indexing Python type stubs.

If type-aware features like autocompletion are not working after installing the package, make sure your editor supports indexing Python type stubs and is set up to index packages in the environment you installed the package into. Sometimes it may also help to restart your editor to make sure newly installed/updated packages are correctly indexed.

After installing the stubs, you can copy the following line to the top of every Python file to have the same imports as the ones that are added by default in the cloud:
```py
from AlgorithmImports import *
```

This line imports [all common QuantConnect members](https://github.com/QuantConnect/Lean/blob/master/Common/AlgorithmImports.py) and provides autocomplete for them.

## Development

To run the generator locally, clone the repository, `cd` into the QuantConnectStubsGenerator project and run `dotnet run <Lean directory> <runtime directory> <output directory>`. Make sure `<Lean directory>` points to a directory containing the [QuantConnect/Lean](https://github.com/QuantConnect/Lean) repository and `<runtime directory>` points to a directory containing the [dotnet/runtime](https://github.com/dotnet/runtime) repository.

To run the unit tests, run `dotnet test` in the root of the project. To run the integration tests read the [`integration/README.md`](./integration/README.md) file.

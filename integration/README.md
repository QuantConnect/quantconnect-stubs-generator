# Integration Tests

This directory contains the integration tests. These are written in Python because the NUnit runners don't seem to consistently log both external process output and `Console.WriteLine` messages, making debugging a lot harder.

Please note that these integration tests are not meant to show no errors at all. Because of the differences between C# and Python, it is sometimes necessary to perform conversions which are invalid according to common PEPs, as long as editors can still read the stubs and provide autocompletion and the like properly.

## Usage

Before running `integration_tests.py`, make sure the following commands are available on your `PATH`:
- `git`, to clone/pull the latest version of Lean
- `dotnet`, to run the generator
- `pyright`, to check the generated stubs using the [Pyright](https://github.com/microsoft/pyright) type checker used in [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) (`npm i -g pyright` or `yarn global add pyright`)

During development it is also useful to check the generated stubs in PyCharm and in VS Code with the [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) extension. Good files to open and see if the stubs provide correct information can be found in [QuantConnect/Lean/Algorithm.Python](https://github.com/QuantConnect/Lean/tree/master/Algorithm.Python).

# QuantConnect Stubs Generator

[![Build Status](https://github.com/QuantConnect/quantconnect-stubs-generator/workflows/Build/badge.svg)](https://github.com/QuantConnect/quantconnect-stubs-generator/actions?query=workflow%3ABuild)

QuantConnect Stubs Generator is a program which generates Python stubs based on the C# files in [QuantConnect/Lean](https://github.com/QuantConnect/Lean) and [dotnet/runtime](https://github.com/dotnet/runtime).

## Installation

Soon: `pip install quantconnect-stubs`.

## Development

To run the generator locally, clone the repository, `cd` into the QuantConnectStubsGenerator project and run `dotnet run <Lean directory> <runtime directory> <output directory>`. Make sure `<Lean directory>` points to a directory containing the [QuantConnect/Lean](https://github.com/QuantConnect/Lean) repository and the `runtime directory` points to a directory containing the [dotnet/runtime](https://github.com/dotnet/runtime) repository.

To run the unit tests, run `dotnet test` in the root of the project. To run the integration tests read [`integration/README.md`](./integration/README.md).

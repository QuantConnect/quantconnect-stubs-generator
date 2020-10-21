# QuantConnect Stubs Generator

[![Build Status](https://github.com/QuantConnect/quantconnect-stubs-generator/workflows/Build/badge.svg)](https://github.com/QuantConnect/quantconnect-stubs-generator/actions?query=workflow%3ABuild)

QuantConnect Stubs Generator is a program which generates Python stubs based on [QuantConnect/Lean](https://github.com/QuantConnect/Lean)'s C# codebase.

## Installation

Soon: `pip install quantconnect-stubs`.

## Development

To run the generator locally, clone the repository, `cd` into the QuantConnectStubsGenerator project and run `dotnet run <Lean directory> <output directory>`.

To run the unit tests, run `dotnet test`. To run the integration tests read [`integration/README.md`](./integration/README.md).

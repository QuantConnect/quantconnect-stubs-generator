# Integration Tests

This directory contains the integration tests. These are written in Python because there NUnit runners don't seem to consistently log both external process output and `Console.WriteLine` messages, making debugging a lot harder.

## Usage

Before running `integration_tests.py`, make sure `git`, `mypy` (`pip install mypy` or `conda install mypy`) and `pyright` (`npm i -g pyright` or `yarn global add pyright`) are available on your `PATH`.

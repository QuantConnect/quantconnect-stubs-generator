# QUANTCONNECT.COM - Democratizing Finance, Empowering Individuals.
# Lean Algorithmic Trading Engine v2.0. Copyright 2014 QuantConnect Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from utils import *

def main():
    if find_spec("QuantConnect") is not None:
        fail("Integration tests must run in an environment in which the stubs are not already installed")

    for package in ["pandas", "matplotlib"]:
        if find_spec(package) is None:
            fail(f"{package} must be installed when running the integration tests")

    ensure_command_availability("git")
    ensure_command_availability("dotnet")
    ensure_command_availability("pyright")
    ensure_command_availability("mypy")

    project_root = Path(__file__).absolute().parent.parent
    generated_dir = project_root / "generated"
    lean_dir = generated_dir / "Lean"
    runtime_dir = generated_dir / "runtime"
    stubs_dir = generated_dir / "stubs"
    generator_dir = project_root / "QuantConnectStubsGenerator"

    generated_dir.mkdir(parents=True, exist_ok=True)

    ensure_repository_up_to_date("QuantConnect/Lean", lean_dir)
    ensure_repository_up_to_date("dotnet/runtime", runtime_dir)

    if stubs_dir.exists():
        shutil.rmtree(stubs_dir)

    if not run_command(["dotnet", "run", lean_dir, runtime_dir, stubs_dir], cwd=generator_dir):
        fail("Could not run QuantConnectStubsGenerator")

    with open(stubs_dir / "pyrightconfig.json", "w") as file:
        file.write(f"""
{{
    "include": [{", ".join([f'"{ns}/**"' for ns in os.listdir(stubs_dir)])}],
    "exclude": ["System/Collections/Immutable/**", "System/__init__.pyi", "System/Runtime/InteropServices/**"],
    "reportGeneralTypeIssues": "none",
    "reportInvalidTypeVarUse": "none",
    "reportWildcardImportFromLibrary": "none"
}}
        """.strip())

    if not run_command(["pyright"], cwd=stubs_dir):
        fail("Pyright found errors in the generated stubs")


    for filename in os.listdir(stubs_dir):
        print(f"FILE: {filename}")

    run_command([sys.executable, "setup.py", "--quiet", "sdist", "bdist_wheel"], cwd=stubs_dir)
    run_command([sys.executable, "-m", "pip", "install", "--force-reinstall", "dist/quantconnect_stubs-16929-py3-none-any.whl"], cwd=stubs_dir)
    run_command([sys.executable, "run_syntax_check.py"], cwd=lean_dir, append_empty_line=False)

if __name__ == "__main__":
    main()

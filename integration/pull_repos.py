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

from utils import *

# Simple setup script that gets Lean and runtime repos into our workspace
# under `generated` directory
def main():
    ensure_command_availability("git")
    ensure_command_availability("dotnet")
    ensure_command_availability("pyright")

    project_root = Path(__file__).absolute().parent.parent
    generated_dir = project_root / "generated"
    lean_dir = generated_dir / "Lean"
    runtime_dir = generated_dir / "runtime"
    stubs_dir = generated_dir / "stubs"
    generator_dir = project_root / "QuantConnectStubsGenerator"

    generated_dir.mkdir(parents=True, exist_ok=True)

    ensure_repository_up_to_date("QuantConnect/Lean", lean_dir)
    ensure_repository_up_to_date("dotnet/runtime", runtime_dir)


if __name__ == "__main__":
    main()

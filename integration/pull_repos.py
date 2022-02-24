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

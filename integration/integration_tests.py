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
    "exclude": ["System/Collections/Immutable/**", "System/__init__.pyi", "System/Runtime/InteropServices/__init__.pyi"],
    "reportGeneralTypeIssues": "none",
    "reportInvalidTypeVarUse": "none",
    "reportWildcardImportFromLibrary": "none"
}}
        """.strip())

    if not run_command(["pyright"], cwd=stubs_dir, append_empty_line=False):
        fail("Pyright found errors in the generated stubs")


if __name__ == "__main__":
    main()

import os
import pathlib
import shutil
import subprocess
import sys


def fail(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


def run_command(args, cwd=os.getcwd(), append_empty_line=True):
    try:
        print(f"Running {[str(arg) for arg in args] if len(args) <= 10 else args[0]} in {cwd}", flush=True)
        proc = subprocess.run(args, cwd=cwd)

        if append_empty_line:
            print(flush=True)

        return proc.returncode == 0
    except FileNotFoundError:
        return False


def ensure_command_availability(command):
    if not run_command([command, "--version"]):
        fail(f"{command} is not available")


def ensure_repository_up_to_date(repo, repo_dir):
    if repo_dir.exists():
        if not run_command(["git", "pull"], cwd=repo_dir):
            fail(f"Could not pull {repo}")
    else:
        if not run_command(["git", "clone", "--depth", "1", f"https://github.com/{repo}.git", repo_dir]):
            fail(f"Could not clone {repo}")


def get_python_files(dir):
    for dirpath, _, files in os.walk(dir):
        for file in files:
            if file.endswith(".pyi"):
                yield os.path.abspath(os.path.join(dirpath, file))


def main():
    ensure_command_availability("git")
    ensure_command_availability("dotnet")
    ensure_command_availability("pyright")

    project_root = pathlib.Path(os.getcwd()).parent
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
    "reportGeneralTypeIssues": false,
    "reportMissingModuleSource": false,
    "reportInvalidTypeVarUse": false
}}
        """.strip())

    if not run_command(["pyright"], cwd=stubs_dir, append_empty_line=False):
        fail("Pyright found errors in the generated stubs")


if __name__ == "__main__":
    main()

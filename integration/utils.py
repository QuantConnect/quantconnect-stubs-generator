import os
import shutil
import subprocess
import sys
from importlib.util import find_spec
from pathlib import Path

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
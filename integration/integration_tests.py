import os
import pathlib
import shutil
import subprocess
import sys


def fail(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


def run_command(args, cwd=os.getcwd()):
    try:
        print(f'Running {[str(arg) for arg in args] if len(args) <= 10 else args[0]}', flush=True)
        proc = subprocess.run(args, cwd=cwd)
        print(flush=True)
        return proc.returncode == 0
    except FileNotFoundError:
        return False


def ensure_command_availability(command):
    if not run_command([command, '--version']):
        fail(f'{command} is not available')


def get_python_files(dir):
    for dirpath, _, files in os.walk(dir):
        for file in files:
            if file.endswith('.py'):
                yield os.path.abspath(os.path.join(dirpath, file))


def main():
    ensure_command_availability('git')
    ensure_command_availability('mypy')
    ensure_command_availability('pyright')

    project_root = pathlib.Path(os.getcwd()).parent
    generated_dir = project_root / 'generated'
    lean_dir = generated_dir / 'Lean'
    stubs_dir = generated_dir / 'stubs'
    generator_dir = project_root / 'QuantConnectStubsGenerator'

    generated_dir.mkdir(parents=True, exist_ok=True)

    if lean_dir.exists():
        if not run_command(['git', 'pull'], cwd=lean_dir):
            fail('Could not pull QuantConnect/Lean')
    else:
        if not run_command(['git', 'clone', '--depth', '1', 'https://github.com/QuantConnect/Lean.git', lean_dir]):
            fail('Could not clone QuantConnect/Lean')

    if stubs_dir.exists():
        shutil.rmtree(stubs_dir)

    if not run_command(['dotnet', 'run', lean_dir, stubs_dir], cwd=generator_dir):
        fail('Could not run QuantConnectStubsGenerator')

    mypy_success = run_command(['mypy'] + [file for file in get_python_files(stubs_dir)], cwd=stubs_dir)
    pyright_success = run_command(['pyright', 'Oanda', 'QuantConnect'], cwd=stubs_dir)

    if not mypy_success and not pyright_success:
        fail('Mypy and Pyright found errors')
    elif not mypy_success:
        fail('Mypy found errors')
    elif not pyright_success:
        fail('Pyright found errors')


if __name__ == '__main__':
    main()

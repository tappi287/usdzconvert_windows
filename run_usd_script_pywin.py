#!usr/bin/python3
"""
    This will setup an appropriate OS environment to run Python USD scripts from usdzconvert script path
"""
import os
import sys
from pathlib import Path, WindowsPath
from subprocess import Popen

DEBUG = 0  # Print Environment info


def update_path_string(env: dict, key: str, new_path: Path):
    env_path_string = env.get(key, '')
    if DEBUG:
        print(f'Extending {key} with: {new_path}')

    if not env_path_string:
        env[key] = f'{WindowsPath(new_path.absolute())};'
    elif env_path_string[-1:] == ';':
        env[key] = f'{env_path_string}{WindowsPath(new_path.absolute())};'
    else:
        env[key] = f'{env_path_string};{WindowsPath(new_path.absolute())};'


def create_usd_env():
    base = Path(__file__).parent / 'USD'
    deps = base / 'deps'
    libp = base / 'lib'
    pyp = base / 'lib' / 'python'

    embree_deps = deps / 'embree'
    python_deps = deps / 'python'
    usdview_deps = deps / 'usdview-deps'
    usdview_python_deps = deps / 'usdview-deps-python'

    usdz_python_path = Path(__file__).parent / 'usdzconvert'

    # Create a copy of the actual os environment
    env = dict()
    env.update(os.environ)

    if not base.exists():
        return env

    # Update PYTHONPATH
    for p in (pyp, usdview_python_deps, usdz_python_path):
        update_path_string(env, 'PYTHONPATH', p)

    # Update PATH
    for p in (python_deps, libp, usdview_deps, embree_deps):
        update_path_string(env, 'PATH', p)

    return env


if __name__ == '__main__':
    if DEBUG:
        print(sys.argv)

    usd_env = create_usd_env()
    py_path = Path(__file__).parent / 'USD' / 'deps' / 'python' / 'python.exe'  # Python 2.7

    t = [WindowsPath(py_path.absolute())]

    if not len(sys.argv) > 1:
        print('Not enough arguments. See the example usage below:')
        print("python run_usd_script_pywin.py 'usdzconvert/usdzconvert' 'inputFile' '-iOS12'")
        sys.exit(-1)

    for arg in sys.argv[1:]:
        # Omit first argument which will be path to this script file
        print(arg)
        t.append(arg)

    exitcode = Popen(t, env=usd_env).wait()
    sys.exit(exitcode)

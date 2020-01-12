"""
    Python 2 and 3 version

    This will setup an appropriate OS environment to run Python USD scripts from usdzconvert script path
"""
from __future__ import print_function
import os
import sys
from subprocess import Popen

DEBUG = 1  # Print Environment info


def join(*args):
    return os.path.join(*args)


def update_path_string(env, key, new_path):
    if not os.path.exists(new_path):
        print('Skipping non-existing path:', new_path)
        return

    env_path_string = env.get(key, '')
    if DEBUG:
        print('Extending {} with: {}'.format(key, os.path.abspath(new_path)))

    if not env_path_string:
        env[key] = os.path.abspath(new_path) + os.pathsep
    elif env_path_string[-1:] == os.pathsep:
        env[key] = env_path_string + os.path.abspath(new_path) + os.pathsep
    else:
        env[key] = env_path_string + os.pathsep + os.path.abspath(new_path) + os.pathsep


def create_usd_env():
    base = join(os.path.dirname(__file__), 'USD')
    usd_lib = join(base, 'lib')
    usd_bin = join(base, 'bin')
    usd_plg = join(base, 'plugin', 'usd')
    usd_python_lib = join(base, 'lib', 'python')

    # Unix specific
    ld_lib = join(base, 'lib64')

    # Windows specific portable python2.7 interpreter and p2.7 modules
    _deps = join(base, 'deps')
    python_deps = join(_deps, 'python')
    usdview_python_deps = join(_deps, 'usdview-deps-python')

    usdzconvert_python_path = join(os.path.dirname(__file__), 'usdzconvert')

    # Create a copy of the actual os environment
    env = dict()
    env.update(os.environ)
    if sys.platform == 'win32':
        env['PATH'] = str()  # This will not work on Unix, it would no longer find the python executable

    if not os.path.exists(base):
        return env

    # Update LD_LIBRARY_PATH
    if os.path.exists(ld_lib):
        update_path_string(env, 'LD_LIBRARY_PATH', ld_lib)

    # Update PYTHONPATH
    for p in (usdzconvert_python_path, usdview_python_deps, usd_python_lib):
        update_path_string(env, 'PYTHONPATH', p)

    # Update PATH
    for p in (python_deps, usd_lib, usd_bin, usd_plg):
        update_path_string(env, 'PATH', p)

    return env


if __name__ == '__main__':
    if DEBUG:
        print(sys.argv)

    usd_env = create_usd_env()

    if sys.platform == 'win32':
        py_path = join(os.path.dirname(__file__), 'USD', 'deps', 'python', 'python.exe')  # Python 2.7
        arguments = [os.path.abspath(py_path)]
    else:
        arguments = ['python2.7']

    if not len(sys.argv) > 1:
        print("##########################################################################")
        print("No arguments provided, running python2.7 interpreter with USD environment.")
        print("##########################################################################")
        p = Popen(arguments, env=usd_env)
        out, error = p.communicate()
        sys.exit(p.returncode)

    for arg in sys.argv[1:]:
        # Omit first argument which will be path to this script file
        print(arg)
        arguments.append(arg)

    p = Popen(arguments, env=usd_env)
    out, error = p.communicate()
    sys.exit(p.returncode)

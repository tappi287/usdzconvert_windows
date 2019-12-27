#!usr/bin/python2
"""
    This will setup an appropriate OS environment to run Python USD scripts from usdzconvert script path
    Python 2.7 version
"""
import os
import sys
from subprocess import Popen

DEBUG = 0  # Print Environment info


def join(*args):
    return os.path.join(*args)


def update_path_string(env, key, new_path):
    env_path_string = env.get(key, '')
    if DEBUG:
        print 'Extending {} with: {}'.format(key, new_path)

    if not env_path_string:
        env[key] = os.path.abspath(new_path) + ';'
    elif env_path_string[-1:] == ';':
        env[key] = env_path_string + os.path.abspath(new_path) + ';'
    else:
        env[key] = env_path_string + ';' + os.path.abspath(new_path) + ';'


def create_usd_env():
    base = join(os.path.dirname(__file__), 'USD')
    deps = join(base, 'deps')
    libp = join(base, 'lib')
    pyp = join(base, 'lib', 'python')

    embree_deps = join(deps, 'embree')
    python_deps = join(deps, 'python')
    usdview_deps = join(deps, 'usdview-deps')
    usdview_python_deps = join(deps, 'usdview-deps-python')

    usdz_python_path = join(os.path.dirname(__file__), 'usdzconvert')

    # Create a copy of the actual os environment
    env = dict()
    env.update(os.environ)

    if not os.path.exists(base):
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
        print sys.argv

    usd_env = create_usd_env()
    py_path = join(os.path.dirname(__file__), 'USD', 'deps', 'python', 'python.exe')  # Python 2.7

    arguments = [os.path.abspath(py_path)]

    if not len(sys.argv) > 1:
        print 'Not enough arguments. See the example usage below:'
        print "python run_usd_script_pywin.py 'usdzconvert/usdzconvert' 'inputFile' '-iOS12'"
        sys.exit(-1)

    for arg in sys.argv[1:]:
        # Omit first argument which will be path to this script file
        print arg
        arguments.append(arg)

    exitcode = Popen(arguments, env=usd_env).wait()
    sys.exit(exitcode)

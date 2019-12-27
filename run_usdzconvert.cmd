@echo off
setlocal
pushd %~dp0

set DEPS=%~dp0\USD\deps
set LIBP=%~dp0\USD\lib
set PYP=%~dp0\USD\lib\python

set EMBREE_DEPS=%DEPS%\embree
set PYTHON_DEPS=%DEPS%\python
set USDVIEW_DEPS=%DEPS%\usdview-deps
set USDVIEW_PYTHON_DEPS=%DEPS%\usdview-deps-python

set PYTHONPATH=%PYP%;%USDVIEW_PYTHON_DEPS%

set PATH=%PYTHON_DEPS%;%LIBP%;%USDVIEW_DEPS%;%EMBREE_DEPS%

@python "%~dp0/usdzconvert/usdzconvert" %*

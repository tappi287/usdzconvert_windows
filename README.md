# usdzconvert_windows
Use Apples usdzconvert on Windows platform

This repository contains command line scripts to run Apples `usdzconvert` with Nvidias pre-build USD libraries on MS Windows. The scripts will create and set appropriate PYTHONPATH and PATH variables so the Apple scripts can locate their dependencies.

Usage:
  - Download the latest [release](https://github.com/tappi287/usdzconvert_windows/releases)
  - Extract the release folder `usd_python_win_27` and open a command line inside that folder
  
  
  - with Python 3 installed:
  		python run_usd_script_pywin.py /usdzconvert/usdzconvert <inputFile> <options>
  - with Python 2 installed:
		python run_usd_script_pywin27.py /usdzconvert/usdzconvert <inputFile> <options>
  - without Python installed:
  		run_usdzconvert.cmd /usdzconvert/usdzconvert <inputFile> <options>
		
  - to use any of the provided utilities
		python run_usd_script_pywin.py /usdzconvert/<utility>.py <inputFile> <options>
------------

#### From the [original usdpython Apple Readme](https://github.com/tappi287/usdzconvert_windows/blob/master/README_USD-Python-Tools.md):
This archive contains
- `usdzconvert`, a Python-based tool to convert from various file formats to usdz
- `usdARKitChecker`, a Python-based tool for usdz validation
- precompiled macOS Python modules for Pixar's USD library
- a set of sample scripts that demonstrate how to write usd files
- the `fixOpacity` tool
- usdzcreateassetlib, a standalone tool to generate an asset library from multiple assets

The easiest way to start using these command-line tools is to double-click `USD.command` in the Finder. This will open a Terminal window with all necessary environment variables set.

For more details, including demos, see the WWDC 2019 session "Working with USD": 
https://developer.apple.com/videos/play/wwdc2019/602/

## [USD Pre-built Libraries and Tools](https://developer.nvidia.com/usd#binaries) by Nvidia
Provided by Nvidia under Modified Apache 2.0 License
These are the pre-built USD Libraries including a Python 2.7 interpreter and provide the USD functionality.

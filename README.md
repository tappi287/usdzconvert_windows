# usdzconvert_windows
Use Apples usdzconvert on Windows or Unix platform

This repository contains command line scripts to run Apples `usdzconvert` with pre-built/pre-compiled USD libraries on MS Windows and Unix(tested on Ubuntu 18.04). The scripts will create and set appropriate PYTHONPATH and PATH variables so the USD libraries and Apple scripts can locate their dependencies.

Usage:
  - Download the latest [release](https://github.com/tappi287/usdzconvert_windows/releases)

  - Extract the release folder `<release_zip_name>` and open a command line inside that folder

  - with Python 2 or 3 installed:
  		`python run_usd.py /usdzconvert/usdzconvert <inputFile> <options>`

  - without Python installed[Windows]:
  		`run_usdzconvert.cmd /usdzconvert/usdzconvert <inputFile> <options>`

  - to use any of the provided utilities
		`python run_usd.py /USD/bin/usdview <inputFile>`
		
  - test usdview with example asset
		`test_usdview_island.cmd`

  ### Unix
  
  - Unix needs a Python 2.7 interpreter with the following packages
    `python2.7 -m pip install --user numpy`<br />
    `python2.7 -m pip install --user Pillow`
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

------------

#### USD Pre-built libraries ####
USD Build 20.2 (latest dev) build with courtesy to [usd-build-club](https://github.com/vfxpro99/usd-build-club). Version info added where necessary due compile errors on Windows 10/VS 2017 15.9.18/Cmake 3.16.2
 - Alembic 1.6.0 (git checkout a3aa758)
 - tbb44_20160526oss [github-release](https://github.com/intel/tbb/releases/download/4.4.5/tbb44_20160526oss_win.zip)
 - ptex v2.2.1
 - OpenSubdiv v3_3_3 (also required pre-compiled [GLFW v3.3](https://github.com/glfw/glfw/releases/download/3.3/glfw-3.3.bin.WIN64.zip))
 - openexr
 - openimageio
 - [boost-build-club](https://github.com/vfxpro99/boost-build-club)
 - [glew-build-club](https://github.com/vfxpro99/glew-build-club)
 - zlib
 - libtiff
 - libpng
 - libjpeg-turbo

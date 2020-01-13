# usdzconvert_windows
Use Apples usdzconvert on Windows or Unix platform with pre-built USD library

This repository contains command line scripts to run Apples `usdzconvert` with pre-built/pre-compiled USD libraries on MS Windows and Unix(tested on Ubuntu 18.04). The scripts will create and set appropriate PYTHONPATH and PATH variables so the USD libraries and Apple scripts can locate their dependencies.

Usage:
  - Download the latest [release](https://github.com/tappi287/usdzconvert_windows/releases)

  - Extract the release folder `<release_zip_name>` and open a command line inside that folder

  - with Python 2 or 3 installed:<br />
  		`python run_usd.py /usdzconvert/usdzconvert <inputFile> <options>`<br />
		`python run_usd.py` - will start an interactive python interpreter with USD environment

  - without Python installed[Windows]:<br />
  		`run_usdzconvert.cmd /usdzconvert/usdzconvert <inputFile> <options>`

  - to use any of the provided utilities<br />
		`python run_usd.py /USD/bin/usdview <inputFile>`
		
  - test usdview with example asset<br />
		`test_usdview_island.cmd`

  ### Unix
  
  - Unix needs a Python 2.7 interpreter with the following packages<br />
		`python2.7 -m pip install --user numpy`<br />
		`python2.7 -m pip install --user Pillow`
    
  - with python2.7 installed:<br />
		`python run_usd.py /usdzconvert/usdzconvert <inputFile> <options>`<br />
		`python run_usd.py` - will start an interactive python interpreter with USD environment
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
* Windows <br />
USD/build_scripts: <br />
```
python build_usd.py "<install_dir>" --build-args USD,"-DBOOST_ROOT=<path_to_boost_binaries>" --openimageio --usdview --alembic --hdf5
````
Fix OpenExr 2.2.0 build errors by copying: Half.dll, Iex-2_2.dll, IexMath-2_2.dll, Imath-2_2.dll to OpenExr build dir\IlmImf (where b44ExpLogTable executable lives).
Using 1_65_1 boost binaries from [SourceForge](https://sourceforge.net/projects/boost/files/boost-binaries/)

* Unix <br />
USD/build_scripts:<br />
`python2.7 build_usd.py --no-imaging --no-usdview --alembic --hdf5` <br />
Fix OpenExr 2.2.0 build errors by: `sudo apt-get install libilmbase-dev`

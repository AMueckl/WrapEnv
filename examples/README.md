# Demonstration of Use of the WrapEnv Package

## Introduction

This is a demonstration of the use of the WrapEnv package. 

The package is intended to be used for wrapping functions that are to be called in a 
different environment an may be subject to pre- or postprocessing of arguments or iterations
based on results of executions and possible modifications.

## Installation

As usual, you can install the package using pip:

```bash
pip install wrapenv
```

## Usage

The package provides an instance of the class `ENVIRONMENT` that can be used as a decorator for functions that
are to be wrapped. As the instance is a global variable, it can be used from anywhere in the code.

For example the PyInstaller issue mentioned in the [Discussion](https://github.com/orgs/pyinstaller/discussions/7645)
stopping the import of some modules of packages of which parts have been frozen for importing can be solved by
using this WrapEnv environment.

The following steps are necessary for making this work:
1. create a PyInstaller .spec file using `pyi-makespec main.py`
2. make a copy of the `main.spec` file to `main_special.spec` add the following lines to the `main_special.spec` file:
```python
    # add the following lines to the .spec file:
   from wrapenv import environment

    environment.register_function(Analysis)
    environment['DISTPATH'] = DISTPATH      # the path to the distribution folder, comes in handy for further postprocessing
```
3. modify the `Analysis` function to use the environment:
```python
    a = environment.Analysis(
    ...
    )
```
4. create a run_pyinstaller.py script to define and inject preprocessing-, checking- /modifying-  and postprocessing 
   functions as shown in the accompanying example [run_pyinstaller.py](run_pyinstaller.py).

   Note: The `run_pyinstaller.py` script also imports the `wrapenv.environment` and thus can register functions for
   preprocessing, checking and modifications to arguments and the environment for the PyInstaller `Analysis` method.
   In this example it is used to check the packages available in the standard Python installation and compares the 
   list with frozen imports of the PyInstaller Analysis method. If there are packages missing, the script will add
   them as hidden imports to the `Analysis` method and start over until there are no more additional packages missing.

5. execute the run_pyinstaller.py script using `python run_pyinstaller.py main.spec`


Note: If you want to try out this examples yourself, you will need to install the package `PyInstaller` using pip.

```bash
pip install PyInstaller
```


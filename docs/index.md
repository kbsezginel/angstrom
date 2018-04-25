[![Build Status](https://travis-ci.org/kbsezginel/angstrom.svg?branch=master)](https://travis-ci.org/kbsezginel/angstrom)
[![codecov](https://codecov.io/gh/kbsezginel/angstrom/branch/master/graph/badge.svg)](https://codecov.io/gh/kbsezginel/angstrom)

# Ångström
A Python package for basic molecular operations with low-dependency and easy-integration.
Ångström offers high quality molecular visualization from the command-line.
It provides easy integration with visualization software such as:
- [Blender](https://www.blender.org/)
- [OpenBabel](http://openbabel.org/wiki/Main_Page), 
- [VMD](http://www.ks.uiuc.edu/Research/vmd/)
- [Nglview](https://github.com/arose/nglview) for visualization.

## About
Ångström is a Python package for geometric molecular operations, molecular visualization and animations.
The purpose of Ångström is to be a lightweight and easily integrable package.
This way it can be easily included in various simulation packages.

-----------------------
**Ångström is currently in development... Stay tuned**

## Installation
You can install Ångström by cloning this repository as follows:
```
git clone https://github.com/kbsezginel/angstrom.git
cd angstrom
python setup.py install
```

### Visualization
In order to make sure all visualization features are avaiable you need to install additional software.
Take a look at [visualization](visualization) page to read more about installation and usage of these software
and visualizing molecules using Ångström.

Ångström will also be available through `pip` in near future.

## Tests
Unit tests are available using [pytest](https://docs.pytest.org/en/latest/).
You can run the tests by executing `pytest` in the main repository.
There will be warnings but if you would liek to suppress warnings messages you can use `pytest --disable-pytest-warnings`.

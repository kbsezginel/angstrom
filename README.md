<p align="center">
<a href="https://travis-ci.org/kbsezginel/angstrom">
  <img src="https://travis-ci.org/kbsezginel/angstrom.svg?branch=master" alt="Travis CI"/>
</a>
<a href="https://ci.appveyor.com/project/kbsezginel/angstrom">
  <img src="https://ci.appveyor.com/api/projects/status/lcj1f73iet2gt5up?svg=true" alt="AppVeyor"/>
</a>
<a href="https://codecov.io/gh/kbsezginel/angstrom">
  <img src="https://codecov.io/gh/kbsezginel/angstrom/branch/master/graph/badge.svg" alt="Codecov"/>
</a>
<a href='https://angstrom.readthedocs.io/en/latest/?badge=latest'>
    <img src='https://readthedocs.org/projects/angstrom/badge/?version=latest' alt='Documentation Status' />
</a>
</p>

<p align="center"><img src="https://raw.githubusercontent.com/kbsezginel/angstrom/master/docs/assets/img/angstrom-logo.png"></p>

Ångström is a Python package for geometric molecular operations, molecular visualization and animations.
The purpose of Ångström is to be a lightweight and easily integrable package.
This way it can be easily included in various simulation packages.
Ångström offers high quality molecular visualization from the command-line.
It provides easy integration with visualization software such as:
-   [Blender](https://www.blender.org/)
-   [OpenBabel](http://openbabel.org/wiki/Main_Page)
-   [VMD](http://www.ks.uiuc.edu/Research/vmd/)
-   [Nglview](https://github.com/arose/nglview) for visualization.

## Installation
You can install Ångström by cloning this repository as follows:
```
git clone https://github.com/kbsezginel/angstrom.git
cd angstrom
python setup.py install
```

## Documentation
Ångström documentation is available on [readthedocs](https://angstrom.readthedocs.io/en/latest/).

### Visualization
In order to make sure all visualization features are available you need to install additional software.
Take a look at [visualization](https://kbsezginel.github.io/angstrom/visualization) page to read more about installation and usage of these software
and visualizing molecules using Ångström.

## Tests
Unit tests are available using [pytest](https://docs.pytest.org/en/latest/).
You can run the tests by executing `pytest` in the main repository.
There will be warnings but if you would like to suppress warnings messages you can use `pytest --disable-pytest-warnings`.

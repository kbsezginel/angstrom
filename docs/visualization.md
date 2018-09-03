Visualization
=============

Ångström offers several ways to visualize molecules and create animations.
Current selections are using [Blender](https://www.blender.org/), [OpenBabel](http://openbabel.org/wiki/Main_Page),
[VMD](http://www.ks.uiuc.edu/Research/vmd/), and [Nglview](https://github.com/arose/nglview) for visualization.
You can render images of molecules using Blender and OpenBabel, render animations using Blender and VMD and
visualize molecules in Jupyter Notebook using Nglview.

Currently, only images can be rendered using Blender and OpenBabel and nglview in Jupyter notebook. The animation future will be implemented soon...

Command-line interface
----------------------
Ångström comes with a command-line interface (`ngstrom-vis`) which you can use to visualize molecules:
```
angstrom-vis tests/C60.pdb
```
To see options:
```
angstrom-vis --help
```

Library usage
-------------
You can also use the rendering capabilities as a part of the Python library:
```python
from angstrom.visualize import render
from angstrom import Molecule


mol = Molecule(read='molecule.xyz')

# Blender rendering
render(mol, 'molecule.png', renderer='blender')

# OpenBabel rendering
render(mol, 'molecule.svg', renderer='openbabel')
```

Blender
-------

### Setup
Make sure you install [Blender](https://www.blender.org/) first.
To use Blender with Ångström you need to make sure the `blender` executable is accessible through Python
[subprocess library](https://docs.python.org/3/library/subprocess.html).
Using Linux `blender` executable is added to PATH with installation both in Windows or Mac this might not be the case.
Make sure you can run blender from the command line.
([This documentation might help.](https://docs.blender.org/manual/en/dev/render/workflows/command_line.html))

After you locate the `blender` executable make sure it is defined correctly in the settings. By default if you can render images using Blender and Ångström than the executable is working.
If not you can setup the executable as follows:
```python
from angstrom.visualize.blender import Blender


# Mac OS example
blend = Blender()
blend.config['executable'] = './blender.app/Contents/MacOS/blender'

# Windows example
blend.config['executable'] = 'C:\\Program Files\\Blender Foundation\\Blender\\blender.exe'
```

If you want to permanently change the executable then you can modify the source code.
Go to `angstrom/visualize/blender.py` and change the `executable` keyword argument of the configure method.

Blender is run from the command line using the following line:
```
blender --background --python myscript.py
```

### Usage and customization

```python
from angstrom.visualize import render
from angstrom.visualize.blender import Blender
from angstrom import Molecule


mol = Molecule(read='molecule.xyz')

blend = Blender()
blend.configure(model='space_filling', camera_zoom=30, camera_type='ORTHO',
                brightness=1.2, resolution=[3000, 2000])

# Render using above configuration
render(mol, 'molecule.png', renderer=blend)
```

OpenBabel
---------

### Setup
To be able to use OpenBabel rendering you need to install OpenBabel first.
Ångström uses `openbabel` executable in order to run OpenBabel for saving images.
Make sure you can run `openbabel` in a terminal in Linux and Mac OS or in command prompt in Windows.

The default command in Ångström runs the following line using Python
[subprocess library](https://docs.python.org/3/library/subprocess.html).
```
obabel molecule.pdb -O molecule.svg -xS -xd xb none
```
where `molecule.pbd` is the `pdb` file to be visualized and `molecule.svg` is the image file to be saved.

### Usage and customization

```python
from angstrom.visualize import render
from angstrom.visualize.openbabel import OpenBabel
from angstrom import Molecule


mol = Molecule(read='molecule.xyz')

ob = OpenBabel()
ob.executable = 'obabel
ob.config = ['-xS', '-xd', 'xb', 'none']

# Render using above configuration
render(mol, 'molecule.svg', renderer=ob)
```


Rendering Animations
--------------------

### Blender

### VMD

```
vmd -dispdev text -eofexit < vis-state.vmd
```

Jupyter Notebook
----------------

### Nglview

Browser
-------

### Three.js

### HTML Embed

"""
--- Ångström ---
Render molecular images and animations.
"""
from .blender import Blender
from .openbabel import OpenBabel
from angstrom.molecule.write import write_pdb
import subprocess
import tempfile
import pickle
import os


def render(molecule, img_file, renderer='blender', verbose=False):
    """
    Render Molecule object.

    Parameters
    ----------
    molecule : Molecule
        Ångström Molecule object.
    img_file : str
        File name for the image file to be saved (use .svg for OpenBabel and .png for Blender).
    renderer : str or object
        The renderer can be either a string ('blender' | 'openbabel') or a renderer object.
        Using a string would select default configuration for each renderer.
        To configure renderer settings the renderer object should be initialized separately
        and used here as an argument.
    verbose : bool
        Verbosity.

    Returns
    -------
    None
        Saves image file.

    Notes
    -----
    Blender: 'png' image format is recommended.
    OpenBabel: 'svg' image format is recommended.

    """
    if isinstance(renderer, str):
        renderer = {'blender': Blender(), 'openbabel': OpenBabel()}[renderer]
    if not hasattr(molecule, 'bonds'):
        molecule.get_bonds()
    temp_pdb_file = tempfile.NamedTemporaryFile(mode='w+', suffix='.pdb')
    write_pdb(temp_pdb_file, molecule.atoms, molecule.coordinates, bonds=molecule.bonds)
    if renderer.__class__.__name__ == 'Blender':
        print('Rendering %s with Blender -> %s' % (molecule.name, img_file))
        renderer.config['pdb']['filepath'] = temp_pdb_file.name
        renderer.config['output'] = img_file
        renderer.config['verbose'] = verbose
        renderer.render_image()
    elif renderer.__class__.__name__ == 'OpenBabel':
        print('Rendering %s with OpenBabel -> %s' % (molecule.name, img_file))
        renderer.verbose = verbose
        renderer.render_image(temp_pdb_file.name, img_file)
    else:
        print('Rendering engine not detected!')
    temp_pdb_file.close()

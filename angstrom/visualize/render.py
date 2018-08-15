"""
--- Ångström ---
Render molecular images and animations.
"""
from .blender import Blender
from angstrom.molecule.write import write_pdb
import subprocess
import tempfile
import pickle
import os


def render(molecule, img_file, renderer=Blender()):
    """
    Render Molecule object.

    Parameters
    ----------
    molecule : Molecule
        Ångström Molecule object.
    img_file : str
        File name for the image file to be saved (use .svg for OpenBabel and .png for Blender).
    renderer : object
        Rendering software object ([Blender] | OpenBabel).

    Returns
    -------
    None
        Saves image file.

    """
    if not hasattr(molecule, 'bonds'):
        molecule.get_bonds()
    temp_pdb_file = tempfile.NamedTemporaryFile(mode='w+', suffix='.pdb')
    write_pdb(temp_pdb_file, molecule.atoms, molecule.coordinates, bonds=molecule.bonds)
    if renderer.__class__.__name__ == 'Blender':
        renderer.config['pdb']['filepath'] = temp_pdb_file.name
        renderer.config['output'] = img_file
        renderer.render_image()
    temp_pdb_file.close()

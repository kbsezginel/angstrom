"""
--- Ångström ---
Render molecular images and animations.
"""
from .render_settings import openbabel_settings
from angstrom.molecule.write import write_pdb
import subprocess
import tempfile


def render(molecule, img_file, renderer='blender', settings=None):
    """ Render Molecule object

    Args:
        - molecule (Molecule): Ångström Molecule object
        - img_file (str): File name for the image file to be saved (use .svg for OpenBabel and .png for Blender)
        - renderer (str): Rendering software ([blender] | openbabel)
        - settings: Rendering settings

    Returns:
        - Saves image file
    """
    if not hasattr(molecule, 'bonds'):
        molecule.get_bonds()
    temp_pdb_file = tempfile.NamedTemporaryFile(mode='w+', suffix='.pdb')
    write_pdb(temp_pdb_file, molecule.atoms, molecule.coordinates, bonds=molecule.bonds)
    if renderer == 'blender':
        render_blender(temp_pdb_file.name, img_file, settings)
    elif renderer == 'openbabel':
        if settings is None:
            settings = openbabel_settings
        render_openbabel(temp_pdb_file.name, img_file, settings)
    temp_pdb_file.close()


def render_openbabel(mol_file, img_file, settings=openbabel_settings):
    """ Render molecular images using OpenBabel

    Args:
        - mol_file (str): Molecule file
        - img_file (str): Image file (recommended file format: svg)
        - settings (list): List of command line arguments
    """
    command = ['obabel', '%s' % mol_file, '-O', '%s' % img_file] + settings
    subprocess.call(command)


def render_blender(mol_file, img_file, settings):
    """ Render molecular images using Blender

    Args:
        - mol_file (str): Molecule file in .pdb format
        - img_file (str): Image file (recommended file format: png)
        - settings (dict): Blender rendering settings
    """
    pass

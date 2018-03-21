"""
--- Ångström ---
Render molecular images and animations.
"""
import subprocess


def render():
    pass


def render_openbabel(mol_file, img_file, arguments=['-xS', '-xd', 'xb', 'none']):
    """ Render molecular images using OpenBabel

    Args:
        - mol_file (str): Molecule file
        - img_file (str): Image file
        - arguments (list): List of command line arguments
    """
    command = ['obabel', '%s' % mol_file, '-O', '%s' % img_file] + arguments
    subprocess.call(command)


def render_blender(mol_file, save=None):
    """ Render molecular images using Blender

    Args:
        - mol_file (str): Molecule file in pdb format
        - save (str or None): Save blender file
    """
    # command = ['obabel', '%s' % mol_file, '-O', '%s' % img_file] + arguments
    if save is not None:
        # Save blender file
    else:
        # Render
    pass

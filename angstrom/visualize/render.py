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

"""
--- Ångström ---
Render molecular images and animations.
"""
from .render_settings import openbabel_settings, get_blender_settings
from angstrom.molecule.write import write_pdb
import subprocess
import tempfile
import pickle
import os


def render(molecule, img_file, renderer='blender', settings=None, verbose=False):
    """
    Render Molecule object.

    Parameters
    ----------
    molecule : Molecule
        Ångström Molecule object.
    img_file : str
        File name for the image file to be saved (use .svg for OpenBabel and .png for Blender).
    renderer : str
        Rendering software ([blender] | openbabel).
    settings : dict or None
        Rendering settings.

    Returns
    -------
    None
        Saves image file.

    """
    if not hasattr(molecule, 'bonds'):
        molecule.get_bonds()
    temp_pdb_file = tempfile.NamedTemporaryFile(mode='w+', suffix='.pdb')
    write_pdb(temp_pdb_file, molecule.atoms, molecule.coordinates, bonds=molecule.bonds)
    if renderer == 'blender':
        if settings is None:
            settings = get_blender_settings()
        render_blender(temp_pdb_file.name, img_file, settings, verbose=verbose)
    elif renderer == 'openbabel':
        if settings is None:
            settings = openbabel_settings
        render_openbabel(temp_pdb_file.name, img_file, settings)
    elif renderer == 'vmd':
        render_vmd(temp_pdb_file.name, img_file, settings, verbose=verbose)
    temp_pdb_file.close()


def render_openbabel(mol_file, img_file, settings=openbabel_settings):
    """
    Render molecular images using OpenBabel.

    Parameters
    ----------
    mol_file : str
        Molecule file.
    img_file : str
        Image file (recommended file format: svg).
    settings : list
        List of command line arguments.

    Returns
    -------
    None
        Saves image file.

    """
    command = ['obabel', '%s' % mol_file, '-O', '%s' % img_file] + settings
    subprocess.call(command)


def render_blender(mol_file, img_file, settings, verbose=False):
    """
    Render molecular images using Blender.

    Parameters
    ----------
    mol_file : str
        Molecule file in .pdb format.
    img_file : str
        Image file (recommended file format: png).
    settings : dict
        Blender rendering settings.
    verbose : bool
        Blender rendering script verbosity.

    Returns
    -------
    None
        Saves image file.

    """
    settings['output'] = img_file
    settings['pdb'] = {**{'filepath': mol_file}, **settings['pdb']}
    # Save options as pickle
    with open(settings['pickle'], 'wb') as handle:
        pickle.dump(settings, handle, protocol=pickle.HIGHEST_PROTOCOL)

    command = [settings['executable'], '--background', '--python', settings['script'], '--', settings['pickle']]
    with open(os.devnull, 'w') as null:
        blend = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = blend.stdout.decode(), blend.stderr.decode()
        if verbose:
            print("Stdout:\n\n%s\nStderr:\n%s" % (stdout, stderr))
    os.remove(settings['pickle'])


def render_vmd(mol_file, img_file, settings, verbose=False):
    """
    Render molecular images using VMD.

    Parameters
    ----------
    mol_file : str
        Molecule file.
    img_file : str
        Image file.
    settings : str
        VMD visualization state file.

    Returns
    -------
    None
        Saves image file.

    """
    input_file = open(settings, 'r')
    command = ['vmd', '-dispdev' 'text']
    vmd = subprocess.run(command, stdin=input_file, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = vmd.stdout.decode(), vmd.stderr.decode()
    input_file.close()
    if verbose:
        print("Stdout:\n\n%s\nStderr:\n%s" % (stdout, stderr))

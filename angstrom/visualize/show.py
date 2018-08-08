"""
--- Ångström ---
Show molecular images and animations.
Works well with Jupyter notebook to visualize molecules in browser.
"""
from .tools import arrange_molecules
from angstrom.molecule.write import write_pdb
import tempfile
import nglview


def show(*molecules, arrange=True, nx=5, distance=(-10, -10), camera='perspective', caps=True, save=None):
    """
    Show molecule objects using nglview.

    Parameters
    ----------
    molecules : Molecule
        Any number Molecule objects.
    arrange : bool
        Arrange structure positions (default: True).
    nx : int
        Number of structures in x axis (horizontal).
    distance : tuple
        Separation distance in x and y axes.
    camera : str
        Camera style -> 'perspective' / 'orthographic'.
    caps : bool
        Make atom names all capital letters (required for nglview to assign correct color).
    save : str or None
        Save visualized structure in pdb format as given filename.

    Returns
    -------
    view
        nglview "view" object.

    """
    atoms, coordinates, group_numbers = arrange_molecules(molecules, arrange=arrange, nx=nx, distance=distance, caps=caps)

    if save is None:
        temp_pdb_file = tempfile.NamedTemporaryFile(mode='w+', suffix='.pdb')
        write_pdb(temp_pdb_file, atoms, coordinates, group=group_numbers)
        view = nglview.show_structure_file(temp_pdb_file.name)
        temp_pdb_file.close()
    else:
        with open(save, 'w') as save_file:
            write_pdb(save_file, atoms, coordinates, group=group_numbers)
        view = nglview.show_structure_file(save)

    view.camera = camera
    return view

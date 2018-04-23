"""
--- Ångström ---
Show molecular images and animations.
Works well with Jupyter notebook to visualize molecules in browser.
"""
from .tools import arrange_molecules
from angstrom.molecule.write import write_pdb
import numpy as np
import tempfile
import nglview


def show(*args, camera='perspective', move='auto', div=5, distance=(-10, -10), axis=0, caps=True, save=None, group=True):
    """
    Show given structures using nglview
        - camera: 'perspective' / 'orthographic'
        - move: separate multiple structures equally distant from each other
        - distance: separation distance
        - axis: separation direction
        - caps: capitalize atom names so they show true colors in nglview
    """
    atoms, coordinates, group_numbers = arrange_molecules(args, move=move, div=div, distance=distance, axis=axis, caps=caps, group=group)

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

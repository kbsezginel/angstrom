"""
--- Ångström ---
Show molecular images and animations.
Works well with Jupyter notebook to visualize molecules in browser.
"""
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
    if move is 'auto':
        translation_vectors = arrange_structure_positions(len(args), div=div, distance=distance)
    elif move is 'single':
        translation_vectors = axis_translation(len(args), distance=distance[0], axis=axis)
    else:
        translation_vectors = [[0, 0, 0]] * len(args)

    atom_names = []
    atom_coors = []
    group_numbers = []
    for mol_index, (molecule, vec) in enumerate(zip(args, translation_vectors), start=1):
        atom_names += molecule.atom_names
        atom_coors += translate(molecule.atom_coors, vector=vec)
        group_numbers += [mol_index] * len(molecule.atom_names)

    # nglview require atom names in all caps to color them properly
    if caps:
        atom_names = [name.upper() for name in atom_names]

    if not group:
        group_numbers = [1] * len(atom_names)

    if save is None:
        temp_pdb_file = tempfile.NamedTemporaryFile(mode='w+', suffix='.pdb')
        write_pdb(temp_pdb_file, atom_names, atom_coors, group=group_numbers)
        view = nglview.show_structure_file(temp_pdb_file.name)
        temp_pdb_file.close()
    else:
        with open(save, 'w') as save_file:
            write_pdb(save_file, atom_names, atom_coors, group=group_numbers)
        view = nglview.show_structure_file(save)

    view.camera = camera
    return view

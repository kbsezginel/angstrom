"""
--- Ångström ---
Visualization tools for arranging molecule positions and more.
"""
import numpy as np


def arrange_molecules(molecules, arrange=True, nx=5, distance=(-10, -10), caps=True):
    """ Arrange molecules in a 2D grid for better visual representation.

    Args:
        - molecules (tuple): Molecule objects.
        - arrange (bool): Arrange structure positions (default: True).
        - nx (int): Number of structures in x axis (horizontal).
        - distance (tuple): Separation distance in x and y axes.
        - caps (bool): Make atom names all capital letters (required for nglview to assign correct color).

    Returns:
        - tuple: Atom coordinates, atom names, and group (residue) numbers.
    """
    n_structures = len(molecules)
    if arrange:
        translation_vectors = arrange_positions(n_structures, nx=nx, distance=distance)
    else:
        translation_vectors = np.zeros((n_structures, 3))

    coordinates = np.concatenate([i.coordinates + v for i, v in zip(molecules, translation_vectors)])
    atoms = np.concatenate([i.atoms for i in molecules])
    group_numbers = [i for i in range(n_structures) for j in range(len(molecules[i].atoms))]

    # nglview require atom names in all caps to color them properly
    if caps:
        atoms = [name.upper() for name in atoms]

    return atoms, coordinates, group_numbers


def arrange_positions(n_structures, nx=5, distance=(10, 10)):
    """ Calculate translation vectors to arrange positions of structures.

    Args:
        - n_structures (int): Total number of structures
        - nx (int): Number of structures in x axis (horizontal)
        - distance (tuple): Separation distance in x and y axes

    Returns:
        - ndarray: Translation vectors to arrange structure positions.
    """
    n_structures_vertical = np.ceil(n_structures / nx)
    ylim = (n_structures_vertical - 1) * distance[1] / 2
    n_structures_horizontal = np.ceil(n_structures / n_structures_vertical)
    xlim = (n_structures_horizontal - 1) * distance[0] / 2

    translation_vectors = np.zeros((n_structures, 3))
    i = 0
    for ycoor in np.arange(ylim + distance[1], -ylim, -distance[1]):
        for xcoor in np.arange(-xlim, xlim + distance[0], distance[0]):
            if i < n_structures:
                translation_vectors[i] = [xcoor, ycoor, 0]
                i += 1
            else:
                break
    return translation_vectors

"""
--- Ångström ---
Visualization tools for arranging molecule positions and more.
"""
import math


def arrange_structure_positions(n_structures, div=5, distance=(10, 10)):
    """
    Arrange structure positions according to number of structures given.
    """
    n_structures_lateral = div
    split = math.ceil(n_structures / n_structures_lateral)
    vertical_positions = axis_translation(split, distance=distance[1], axis=1)
    translation_vectors = []
    for s in range(split):
        if s < 2:
            n_split = math.ceil(n_structures / split)
        else:
            n_split = math.floor(n_structures / split)
        new_vectors = axis_translation(n_split, distance=distance[0], axis=0)
        new_vectors = translate(new_vectors, vector=vertical_positions[s])
        translation_vectors += new_vectors
    return translation_vectors


def translate(atom_coors, vector=[-10, 0, 0]):
    """ Translate given coordinates with given vector """
    translated_coors = []
    x, y, z = vector
    for coor in atom_coors:
        new_coor = [coor[0] + x, coor[1] + y, coor[2] + z]
        translated_coors.append(new_coor)
    return translated_coors


def axis_translation(n_structures, distance=-10, axis=0):
    """
    Automatically adjust structure positions equally distant from each other in given axis
        - distance: distance between each structure
        - axis: axis selection for translation (0: x-axis, 1: y-axis, 2: z-axis)
    """
    translation_vectors = []
    lim = (n_structures - 1) * distance / 2
    for i in range(n_structures):
        vec = [0, 0, 0]
        vec[axis] = -lim + i * distance
        translation_vectors.append(vec)
    return translation_vectors

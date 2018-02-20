"""
--- Ångström ---
Trajectory tools.
"""
from copy import deepcopy
import numpy as np


def non_periodic_coordinates(coordinates, simulation_box, dmin=0.5):
    """Convert periodic simulation coordinates to non-periodic coordinates.
    *** ORTHORHOMBIC CELLS ONLY ***

    Args:
        - coordinates (ndarray): 3D list of atomic coordinates for given number of frames
        - simulation_box (list): Dimensions of the simulation box: [a, b, c]
        - dmin (float): Minimum traveled distance for periodic image jump.
                        If the distance change of a specific atom is bigger than (box_length * dmin)
                        then the atom is assumed to jump to a periodic image.

    Returns:
        - ndarray: 3D list of non-periodic coordinates
    """
    n_frames, n_atoms, _ = np.shape(coordinates)
    nonp_coordinates = np.empty((n_frames, n_atoms, 3))
    nonp_coordinates[0] = deepcopy(coordinates[0])
    for a in range(n_atoms):
        modifier = np.zeros(3)
        for f in range(1, n_frames):
            coor = deepcopy(coordinates[f][a])
            prev_coor = deepcopy(coordinates[f - 1][a])
            for i in range(3):
                dist = coor[i] - prev_coor[i]
                if dist > simulation_box[i] * dmin:
                    modifier[i] -= simulation_box[i]
                elif dist <= -simulation_box[i] * dmin:
                    modifier[i] += simulation_box[i]
                coor[i] += modifier[i]
            nonp_coordinates[f][a] = deepcopy(coor)
    return nonp_coordinates

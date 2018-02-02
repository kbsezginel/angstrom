"""
--- Ångström ---
Trajectory tools.
"""
import numpy as np


def non_periodic_coordinates(coordinates, simulation_box):
    """Convert periodic simulation coordinates to non-periodic coordinates.
    *** ORTHORHOMBIC CELLS ONLY ***

    Args:
        - coordinates (ndarray): 3D list of atomic coordinates for given number of frames
        - simulation_box (list): Dimensions of the simulation box: [a, b, c]

    Returns:
        - ndarray: 3D list of non-periodic coordinates
    """
    n_frames, n_atoms, _ = np.shape(traj.coordinates)
    nonp_coordinates = np.empty((n_frames, n_atoms, 3))
    nonp_coordinates[0] = coordinates[0].copy()
    for a in range(n_atoms):
        modifier = np.zeros(3)
        for f in range(1, n_frames):
            coor = traj.coordinates[f][a].copy()
            prev_coor = traj.coordinates[f - 1][a]
            for i in range(3):
                dist = coor[i] - prev_coor[i]
                if dist > sim_box[i] * 0.5:
                    modifier[i] -= sim_box[i]
                elif dist <= -sim_box[i] * 0.5:
                    modifier[i] += sim_box[i]
                coor[i] += modifier[i]
            nonp_coordinates[f][a] = coor
    return nonp_coordinates

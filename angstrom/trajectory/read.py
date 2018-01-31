"""
--- Ångström ---
Read trajectory from molecular file formats.
"""
import os
import numpy as np


def read_xyz_traj(filename):
    """ Read xyz trajectory and return coordinates as a list.
        Assumes number of atoms is constant.

        Args:
            - filename (str): Trajectory file in xyz format.

        Returns:
            - dict: Trajectory dictionary with atoms, coordinates, timestep and xyz keys
    """
    with open(filename, 'r') as traj_file:
        traj = traj_file.readlines()
    n_atoms = int(traj[0].strip())                # Get number of atoms from first line
    n_frames = int(len(traj) / (n_atoms + 2))     # Calculate number of frames (assuming n_atoms is constant)
    trajectory = {'atoms': np.empty((n_frames, n_atoms), dtype=str),
                  'coordinates': np.empty((n_frames, n_atoms, 3)),
                  'headers': np.empty((n_frames,), dtype=str)}
    for frame in range(n_frames):
        start = frame * (n_atoms + 2)             # Frame start
        end = (frame + 1) * (n_atoms + 2)         # Frame end
        trajectory['coordinates'][frame] = [[float(i) for i in line.split()[1:4]] for line in traj[start + 2:end]]
        trajectory['atoms'][frame] = [line.split()[0] for line in traj[start + 2:end]]
        trajectory['headers'][frame] = (traj[start + 1].strip().split()[2])
    return trajectory

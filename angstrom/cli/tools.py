"""
--- Ångström ---
Command line interface tools.
"""
import shutil

import numpy as np

from angstrom import Trajectory
from angstrom.geometry import Quaternion



def rotation(mol, n_frames, rot_angle, rot_axis, interpolation='linear'):
    """
    Rotate molecule around an axis for given number of frames.
    """
    if interpolation == 'linear':
        angles = np.cumsum(np.full((n_frames,), np.deg2rad(rot_angle / n_frames)))
    elif interpolation == 'sine':
        a = np.deg2rad(rot_angle) / np.pi
        x = np.arange(-np.pi / 2, np.pi / 2, np.pi / n_frames)
        angles = a * np.pi / 2 * np.sin(x) + (np.pi / 2) * a
    n_atoms = len(mol.atoms)
    motion = np.zeros((n_frames + 1, n_atoms, 3))
    Q = Quaternion([0, 1, 1, 1])
    for d_angle, frame in zip(angles, range(n_frames)):
        motion[frame] = np.array([Q.rotation(coor, rot_axis, d_angle).np() for coor in mol.coordinates])
    traj = Trajectory(atoms=np.tile(mol.atoms, n_frames).reshape((n_frames, n_atoms)),
                  coordinates=motion)
    return traj


def search_blender_executable():
    """
    Search for Blender executable in possible locations.
    """
    blender_paths = ['blender',
                     '/Applications/Blender.app/Contents/MacOS/Blender',
                     'C:\\Program Files\\Blender Foundation\\Blender\\blender.exe']
    exe = None
    for path in blender_paths:
        if shutil.which(path) is not None:
            exe = path
    return exe

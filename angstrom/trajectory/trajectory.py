"""
--- Ångström ---
Read, manipulate and analyze molecular trajectory files.
"""
from .read import read_xyz_traj
import numpy as np


class Trajectory:
    """
    Reading and analyzing trajectories in xyz format.
    """
    def __init__(self, read=None):
        """
        Create a trajectory object.
        """
        if read is not None:
            self.read(read)
        else:
            self.atoms = []
            self.coordinates = []

    def __repr__(self):
        """
        Returns basic trajectory info.
        """
        return "<Trajectory atoms: %i | frames: %i | dimensions: %i>" % tuple(np.shape(self.coordinates))

    def __len__(self):
        """
        Returns number of frames.
        """
        return len(self.atoms)

    def read(self, filename):
        """
        Read xyz formatted trajectory file.

        Args:
            - filename (str): Trajectory file name.
        """
        traj = read_xyz_traj(filename)
        self.atoms, self.coordinates, self.headers = traj['atoms'], traj['coordinates'], traj['headers']

"""
--- Ångström ---
Read, manipulate and analyze molecular trajectory files.
"""
from .read import read_xyz_traj
from .write import write_xyz_traj
from angstrom.geometry import get_molecule_center
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

    def write(self, filename):
        """
        Write xyz formatted trajectory file.

        Args:
            -filename (str): Trajectory file name.
        """
        with open(filename, 'w') as traj_file:
            if hasattr(self, 'headers'):
                write_xyz_traj(traj_file, self.atoms, self.coordinates, headers=self.headers)
            else:
                write_xyz_traj(traj_file, self.atoms, self.coordinates)

    def get_center(self, mass=True):
        """
        Get coordinates of molecule center at each frame.

        Args:
            - mass (bool): Calculate center of mass (True) or geometric center (False)

        Returns:
            - ndarray: Molecule center coordinates for each frame.
        """
        centers = np.empty((len(self.atoms), 3))
        for f, (frame_atoms, frame_coors) in enumerate(zip(self.atoms, self.coordinates)):
            centers[f] = get_molecule_center(frame_atoms, frame_coors, mass=mass)
        return centers

    def get_msd(self, coordinates, reference=0):
        """
        Calculate mean squared displcement (MSD) for given 1D coordinates.

        Args:
            - coordinates (ndarray): List of 1D coordinates
            - reference (int): Index for reference frame (default: 0)

        Returns:
            - float: Mean squared displacement

        Example (calculate MSD for the first atom in x direction for each frame):
            >>> traj.get_msd(traj.coordinates[:, 0, 0])
        """
        ref_coor = coordinates[reference]
        return np.average(np.power((coordinates - ref_coor), 2))

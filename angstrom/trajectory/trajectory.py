"""
--- Ångström ---
Read, manipulate and analyze molecular trajectory files.
"""
from .read import read_xyz_traj
from .write import write_xyz_traj
from .tools import non_periodic_coordinates
from angstrom.geometry import get_molecule_center
import numpy as np


class Trajectory:
    """
    Reading and analyzing trajectories in xyz format.
    """
    def __init__(self, atoms=None, coordinates=None, read=None):
        """
        Create a trajectory object.
        """
        if atoms is not None and coordinates is not None:
            self.atoms = atoms
            self.coordinates = coordinates
        elif read is not None:
            self.read(read)
        else:
            self.atoms = []
            self.coordinates = []

    def __repr__(self):
        """
        Returns basic trajectory info.
        """
        return "<Trajectory frames: %i | atoms: %i | dimensions: %i>" % tuple(np.shape(self.coordinates))

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

    def non_periodic(self, simulation_box, dmin=0.5):
        """ Convert periodic simulation trajectory to non-periodic trajectory.
        *** ORTHORHOMBIC CELLS ONLY ***

        Args:
            - simulation_box (list): Dimensions of the simulation box -> [a, b, c]
            - dmin (float): Minimum traveled distance for periodic image jump.
                            If the distance change of a specific atom is bigger than (box_length * dmin)
                            then the atom is assumed to jump to a periodic image.

        Returns:
            - Trajectory: Trajectory object with non-periodic coordinates
        """
        np_traj = Trajectory()
        np_traj.atoms = self.atoms
        np_traj.coordinates = non_periodic_coordinates(self.coordinates, simulation_box, dmin=dmin)
        return np_traj

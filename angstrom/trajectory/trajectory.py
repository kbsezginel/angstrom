"""
--- Ångström ---
Read, manipulate and analyze molecular trajectory files.
"""
from .read import read_xyz_traj
from .write import write_xyz_traj
from angstrom.geometry import get_molecule_center
from angstrom import Molecule
import numpy as np
import os


class Trajectory:
    """
    Reading and analyzing trajectories in xyz format.

    """
    def __init__(self, atoms=None, coordinates=None, read=None, molecule=None):
        """
        Create a trajectory object.

        Parameters
        ----------
        atoms : list or None
            List of elements of the molecule for each frame.
        coordinates : list or None
            List of atomic positions of the molecule for each frame.
        read : str or None
            File name to read molecule file (formats: xyz).
        molecule : Molecule
            Create a Trajectory with 1 frame from a Molecule object.

        """
        self.name = 'Trajectory'
        if atoms is not None and coordinates is not None:
            self.atoms = atoms
            self.coordinates = coordinates
        elif read is not None:
            self.read(read)
        elif molecule is not None:
            self.atoms = np.array([molecule.atoms])
            self.coordinates = np.array([molecule.coordinates])
            self.name = molecule.name
        else:
            self.atoms = []
            self.coordinates = []
        self.current_frame = 0

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

    def __add__(self, traj):
        """
        Trajectory addition for joining the coordinates and elements into a new Trajectory object.

        Parameters
        ----------
        traj : Trajectory
            Trajectory object to be added

        Returns
        -------
        Trajectory
            Joined Trajectory object.

        """
        new_traj = Trajectory(atoms=np.append(self.atoms, traj.atoms, axis=0),
                              coordinates=np.append(self.coordinates, traj.coordinates, axis=0))
        return new_traj

    def __getitem__(self, i):
        """
        Indexing method.
        Returns a Molecule object for given index (frame).
        Returns a Trajectory object if used as slicing.

        """
        if isinstance(i, slice):
            indices = range(len(self))[i.start:i.stop:i.step]
            if len(indices) == 0:
                return []
            else:
                new_traj = Trajectory(molecule=self[indices[0]])
                for j in indices[1:]:
                    new_traj.append(self[j])
                return new_traj
        else:
            return Molecule(atoms=self.atoms[i], coordinates=self.coordinates[i])

    def __iter__(self):
        """
        Initialize iterator, reset frame index.

        """
        self.current_frame = 0
        return self

    def __next__(self):
        """
        Returns the next frame in Trajectory as a Molecule object.

        """
        if self.current_frame >= len(self):
            raise StopIteration

        next_mol = self[self.current_frame]
        self.current_frame += 1
        return next_mol

    def append(self, mol):
        """
        Append molecule to trajectory.
        The number of atoms in the molecule must match that of the trajectory.

        Parameters
        ----------
        mol : Molecule
            Molecule object to be added

        Returns
        -------
        None
            Added to Trajectory object.

        """
        if len(mol.atoms) != self.atoms.shape[1]:
            raise Exception('Trajectory cannot have different number of atoms per frame')
        self.atoms = np.append(self.atoms, [mol.atoms], axis=0)
        self.coordinates = np.append(self.coordinates, [mol.coordinates], axis=0)

    def read(self, filename):
        """
        Read xyz formatted trajectory file.

        Parameters
        ----------
        filename : str
            Trajectory file name.

        Returns
        -------
        None
            Assigns 'coordinates', 'atoms', and 'headers' attributes.

        """
        self.name = os.path.splitext(os.path.basename(filename))[0]
        traj = read_xyz_traj(filename)
        self.atoms, self.coordinates, self.headers = traj['atoms'], traj['coordinates'], traj['headers']

    def write(self, filename):
        """
        Write xyz formatted trajectory file.

        Parameters
        ----------
        filename : str
            Trajectory file name (formats: xyz).

        Returns
        -------
        None
            Writes molecule information to given file name.

        """
        with open(filename, 'w') as traj_file:
            if hasattr(self, 'headers'):
                write_xyz_traj(traj_file, self.atoms, self.coordinates, headers=self.headers)
            else:
                write_xyz_traj(traj_file, self.atoms, self.coordinates)

    def get_center(self, mass=True):
        """
        Get coordinates of molecule center at each frame.

        Parameters
        ----------
        mass : bool
            Calculate center of mass (True) or geometric center (False).

        Returns
        -------
        ndarray
            Molecule center coordinates for each frame.

        """
        centers = np.empty((len(self.atoms), 3))
        for f, (frame_atoms, frame_coors) in enumerate(zip(self.atoms, self.coordinates)):
            centers[f] = get_molecule_center(frame_atoms, frame_coors, mass=mass)
        return centers

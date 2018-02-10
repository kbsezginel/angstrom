"""
--- Ångström ---
Molecule class for Ångström Python package.
"""
from .read import read_xyz
from .write import write_xyz
from angstrom.geometry import get_molecule_center
from angstrom.geometry.quaternion import Quaternion
import os
import numpy as np


class Molecule:
    """
    Molecule class.
    """
    def __init__(self, atoms=None, coordinates=None, read=None):
        """ Molecule class initialization """
        self.name = 'Molecule'
        if atoms is not None and coordinates is not None:
            self.atoms = atoms
            self.coordinates = coordinates
        elif read is not None:
            self.read(read)
        else:
            self.atoms = []
            self.coordinates = []

    def __repr__(self):
        """ Molecule class return """
        return "<Molecule object [%s] with: %s atoms>" % (self.name, len(self.atoms))

    def __add__(self, mol):
        """ """
        new_mol = Molecule(atoms=np.append(self.atoms, mol.atoms),
                           coordinates=np.append(self.coordinates, mol.coordinates, axis=0))
        new_mol.name = '%s+%s' % (self.name, mol.name)
        return new_mol

    def read(self, filename):
        """ Read molecule file.

        Args:
            - filename (str): xyz file name

        Returns:
            - Assigns 'coordinates', 'atoms', and 'header', and 'name' variables.
        """
        self.name = os.path.splitext(os.path.basename(filename))[0]
        mol = read_xyz(filename)
        self.atoms, self.coordinates, self.header = mol['atoms'], mol['coordinates'], mol['header']

    def write(self, filename):
        """ Write molecule file.

        Args:
            - filename (str): xyz file name

        Returns:
            - Writes xyz formatted molecule information to given file name.
        """
        with open(filename, 'w') as xyz_file:
            if hasattr(self, 'header'):
                write_xyz(xyz_file, self.atoms, self.coordinates, self.header)
            else:
                write_xyz(xyz_file, self.atoms, self.coordinates)

    def get_center(self, mass=True):
        """ Get coordinates for molecule center.

        Args:
            - mass (bool): Calculate center of mass (True) or geometric center (False)

        Returns:
            - ndarray: Molecule center coordinates.
        """
        return get_molecule_center(self.atoms, self.coordinates, mass=mass)

    def translate(self, vector):
        """ Translate molecule by given vector.

        Args:
            - vector (ndarray): Translation vector
        """
        self.coordinates += vector

    def rotate(self, axis_point1, axis_point2, angle):
        """ Rotate molecule around an axis defined by two point by a given angle in degrees.
        The direction of rotation is counter-clockwise given that axis is defined as p2 - p1.
        To reverse direction you can multiply angle with -1 or reverse axis points.

        Args:
            - axis_point1 (ndarray): 3D coordinates for the first point that defines axis of rotation
            - axis_point2 (ndarray): 3D coordinates for the second point that defines axis of rotation
            - angle (float): Degree of rotation (angles)

        Example (rotate around y-axis by 90 degrees):
            >>> molecule.rotate([0, 0, 0], [0, 1, 0], 90)
        This would rotate the molecule around y-axis by 90 degrees counter-clockwise.
        """
        Q = Quaternion([0, 1, 1, 1])
        self.coordinates = np.array([Q.rotation(coor, axis_point1, axis_point2, np.radians(angle)).np() for coor in self.coordinates])

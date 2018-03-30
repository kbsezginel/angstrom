"""
--- Ångström ---
Molecule class for Ångström Python package.
"""
from .read import read_xyz
from .write import write_xyz
from .bonds import get_bonds
from .cell import Cell
from angstrom.geometry import get_molecule_center, align_vectors
from angstrom.geometry.quaternion import Quaternion
import os
import numpy as np


class Molecule:
    """
    Molecule class.
    """
    def __init__(self, atoms=None, coordinates=None, read=None):
        """ Molecule class initialization. """
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
        """ Molecule class return. """
        return "<Molecule object [%s] with: %s atoms>" % (self.name, len(self.atoms))

    def __add__(self, mol):
        """ Molecule addition for joining the coordinates and elements into a new molecule object. """
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

    def get_bonds(self):
        """ Estimate molecular bonding. """
        self.bonds = get_bonds(self.atoms, self.coordinates)

    def get_center(self, mass=True):
        """ Get coordinates for molecule center.

        Args:
            - mass (bool): Calculate center of mass (True) or geometric center (False)

        Returns:
            - ndarray: Molecule center coordinates.
        """
        return get_molecule_center(self.atoms, self.coordinates, mass=mass)

    def center(self, coor=[0, 0, 0], mass=True):
        """ Move linker to given coordinates using it's center

        Args:
            - coor (ndarray): Destination coordinate of the molecule
            - mass (bool): Use atomic mass for calculating the center (default: True)
        """
        current_center = self.get_center()
        center_vector = np.array(coor) - current_center
        self.translate(center_vector)

    def translate(self, vector):
        """ Translate molecule by given vector.

        Args:
            - vector (ndarray): Translation vector
        """
        self.coordinates += vector

    def rotate(self, axis_point1, axis_point2, angle, center=False, mass=True):
        """ Rotate molecule around an axis defined by two point by a given angle in degrees.
        The direction of rotation is counter-clockwise given that axis is defined as p2 - p1.
        To reverse direction you can multiply angle with -1 or reverse axis points.
        To rotate molecule on it's local axis use center=True.
        This will prevent the molecule from moving after rotation.

        Args:
            - axis_point1 (ndarray): 3D coordinates for the first point that defines axis of rotation
            - axis_point2 (ndarray): 3D coordinates for the second point that defines axis of rotation
            - angle (float): Degree of rotation (radians)
            - center (bool): Keep the molecule at the same position after rotation (default: False)
            - mass (bool): Use atomic mass for calculating the center (default: True)

        Example (rotate around y-axis by 90 degrees):
            >>> molecule.rotate([0, 0, 0], [0, 1, 0], np.pi)
        This would rotate the molecule around y-axis by 90 degrees counter-clockwise.
        """
        if center:
            current_center = self.get_center(mass=mass)
        Q = Quaternion([0, 1, 1, 1])
        self.coordinates = np.array([Q.rotation(coor, axis_point1, axis_point2, angle).np() for coor in self.coordinates])
        if center:
            self.center(current_center, mass=mass)

    def align(self, mol_vector, align_vector, center=False, mass=True):
        """ Align molecule to given vector using molecule vector.

        Args:
            - mol_vector (ndarray): Molecule vector to be aligned
            - align_vector (ndarray): Target vector to align the molecule
            - center (bool): Keep the molecule at the same position after alignment (default: False)
            - mass (bool): Use atomic mass for calculating the center (default: True)
        """
        alignment = align_vectors(mol_vector, align_vector)
        self.rotate([0, 0, 0], alignment['axis'], alignment['angle'], center=center, mass=mass)

    def set_cell(self, cellpar):
        """ Set cell for molecule.

        Args:
            - cellpar (list): Cell parameters -> [a, b, c, alpha, beta, gamma]
        """
        self.cell = Cell(cellpar, atoms=self.atoms, coordinates=self.coordinates)

    def replicate(self, replication, center=True):
        """ Build a supercell by replicating the cell.

        Args:
            - replication (list): Replication in cell vectors -> [a, b, c]
        """
        supercell = self.cell.supercell(replication, center=center)
        supermol = Molecule(atoms=supercell.atoms, coordinates=supercell.coordinates)
        supermol.cell = supercell
        return supermol

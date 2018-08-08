"""
--- Ångström ---
Molecule class for Ångström Python package.
"""
from .read import read_xyz
from .write import write_molecule
from .bonds import get_bonds
from .cell import Cell
from angstrom.geometry import get_molecule_center, align_vectors
from angstrom.geometry.quaternion import Quaternion
from angstrom.geometry.plane import Plane
import os
import numpy as np
import periodictable


class Molecule:
    """
    Molecule class.
    """
    def __init__(self, atoms=None, coordinates=None, read=None):
        """ Molecule class initialization.

        Parameters
        ----------
        atoms : list or None
            List of elements of the molecule.
        coordinates : list or None
            List of atomic positions of the molecule.
        read : str or None
            File name to read molecule file (formats: xyz).
        """
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
        """ Molecule addition for joining the coordinates and elements into a new molecule object.

        Parameters
        ----------
        mol : Molecule object
            Molecule to add together.

        Returns
        -------
        Molecule
            The joined Molecule object.
        """
        new_mol = Molecule(atoms=np.append(self.atoms, mol.atoms),
                           coordinates=np.append(self.coordinates, mol.coordinates, axis=0))
        new_mol.name = '%s+%s' % (self.name, mol.name)
        return new_mol

    def read(self, filename):
        """ Read molecule file.

        Parameters
        ----------
        filename : str
            Molecule file name (formats: xyz).

        Returns
        -------
        None
            Assigns 'coordinates', 'atoms', and 'header', and 'name' attributes.
        """
        self.name = os.path.splitext(os.path.basename(filename))[0]
        mol = read_xyz(filename)
        self.atoms, self.coordinates, self.header = mol['atoms'], mol['coordinates'], mol['header']

    def write(self, filename, bonds=False, cell=None, header='angstrom', group=None):
        """ Write molecule file.

        Parameters
        ----------
        filename : str
            Molecule file name, file format extracted from file extension (formats: xyz | pdb | cif).
        bonds : bool
            Write atomic bonding (used in pdb format).
        cell : list
            Write unit cell parameters (used in cif format).
        header : str
            Molecule file header.
        group : list
            Atom grouping (used in pdb format).

        Returns
        -------
        None
            Writes molecule information to given file name.
        """
        if bonds:
            if not hasattr(self, 'bonds'):
                self.get_bonds()
            write_molecule(filename, self.atoms, self.coordinates, bonds=self.bonds, cell=cell, header=header, group=group)
        else:
            write_molecule(filename, self.atoms, self.coordinates, bonds=None, cell=cell, header=header, group=group)

    def get_bonds(self):
        """ Estimate molecular bonding.

        Parameters
        ----------
        None

        Returns
        -------
        None
            Assigns 'bonds' attribute.
        """
        self.bonds = get_bonds(self.atoms, self.coordinates)

    def get_molecular_weight(self):
        """ Calculate molecular weight.

        Parameters
        ----------
        None

        Returns
        -------
        float
            Molecular weight of the Molecule object..
        """
        return sum([periodictable.elements.symbol(atom).mass for atom in self.atoms])

    def get_center(self, mass=True):
        """ Get coordinates for molecule center.

        Parameters
        ----------
        mass : bool
            Calculate center of mass (True) or geometric center (False).

        Returns
        -------
        ndarray
            Molecule center coordinates.
        """
        return get_molecule_center(self.atoms, self.coordinates, mass=mass)

    def center(self, coor=[0, 0, 0], mass=True):
        """ Move linker to given coordinates using it's center

        Parameters
        ----------
        coor : ndarray
            Destination coordinate of the molecule.
        mass : bool
            Use atomic mass for calculating the center (default: True).

        Returns
        -------
        None
            Modifies 'coordinates' attribute of the Molecule object by calling the 'translate' method.
        """
        current_center = self.get_center()
        center_vector = np.array(coor) - current_center
        self.translate(center_vector)

    def translate(self, vector):
        """ Translate molecule by given vector.

        Parameters
        ----------
        vector : ndarray
            Translation vector.

        Returns
        -------
        None
            Modifies 'coordinates' attribute of the Molecule object.
        """
        self.coordinates += vector

    def rotate(self, axis_point1, axis_point2, angle, center=False, mass=True):
        """ Rotate molecule around an axis defined by two point by a given angle in degrees.
        The direction of rotation is counter-clockwise given that axis is defined as p2 - p1.
        To reverse direction you can multiply angle with -1 or reverse axis points.
        To rotate molecule on it's local axis use center=True.
        This will prevent the molecule from moving after rotation.

        Example (rotate around y-axis by 90 degrees):
            >>> molecule.rotate([0, 0, 0], [0, 1, 0], np.pi)
        This would rotate the molecule around y-axis by 90 degrees counter-clockwise.

        Parameters
        ----------
        axis_point1 : list
            3D coordinates for the first point that defines axis of rotation.
        axis_point2 : list
            3D coordinates for the second point that defines axis of rotation.
        angle : float
            Degree of rotation (radians).
        center : bool
            Keep the molecule at the same position after rotation (default: False).
        mass : bool
            Use atomic mass for calculating the center (default: True).

        Returns
        -------
        None
            Modifies 'coordinates' attribute of the Molecule object.
        """
        if center:
            current_center = self.get_center(mass=mass)
        Q = Quaternion([0, 1, 1, 1])
        self.coordinates = np.array([Q.rotation(coor, axis_point1, axis_point2, angle).np() for coor in self.coordinates])
        if center:
            self.center(current_center, mass=mass)

    def reflect(self, plane, translate=None):
        """ Get mirror image of a molecule by reflecting each atom through a plane of reflection.

        Parameters
        ----------
        plane : Plane
            Mirror plane defined by either 3 points or a string (ex: 'xy') for main planes.
        translate : float or None
            Translate the molecule after reflection by given amount on the axis normal to the plane.

        Returns
        -------
        None
            Modifies 'coordinates' attribute of the Molecule object.
        """
        self._set_plane(plane)
        self.coordinates = np.array([self.plane.reflect(i) for i in self.coordinates])
        if translate is not None:
            self.translate(np.array([self.plane.a, self.plane.b, self.plane.c]) * translate)

    def _set_plane(self, args):
        """ Set plane of reflection. """
        self.plane = Plane(args)

    def align(self, mol_vector, align_vector, center=False, mass=True):
        """ Align molecule to given vector using molecule vector.

        Parameters
        ----------
        mol_vector : ndarray
            Molecule vector to be aligned.
        align_vector : ndarray
            Target vector to align the molecule.
        center : bool
            Keep the molecule at the same position after alignment (default: False).
        mass : bool
            Use atomic mass for calculating the center (default: True).

        Returns
        -------
        None
            Modifies 'coordinates' attribute of the Molecule object.
        """
        alignment = align_vectors(mol_vector, align_vector)
        self.rotate([0, 0, 0], alignment['axis'], alignment['angle'], center=center, mass=mass)

    def set_cell(self, cellpar):
        """ Set cell for molecule.

        Parameters
        ----------
        cellpar : list
            Cell parameters -> [a, b, c, alpha, beta, gamma].

        Returns
        -------
        None
            Assigns 'cell' attribute as a Cell object.
        """
        self.cell = Cell(cellpar)

    def replicate(self, replication, center=True):
        """ Build a supercell by replicating the cell.

        Parameters
        ----------
        replication : list
            Replication in cell vectors -> [a, b, c].

        Returns
        -------
        Molecule
            The replicated Molecule object.
        """
        supercell, atoms, coors = self.cell.supercell(self.atoms, self.coordinates, replication, center=center)
        supermol = Molecule(atoms=atoms, coordinates=coors)
        supermol.cell = supercell
        return supermol

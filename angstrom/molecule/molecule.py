"""
--- Ångström ---
Molecule class for Ångström Python package.
"""
import os
from .read import read_xyz
from .write import write_xyz
from angstrom.geometry import get_molecule_center


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

    def read(self, filename):
        """ Read molecule file
        Args:
            - filename (str): xyz file name

        Returns:
            - Assigns 'coordinates', 'atoms', and 'header', and 'name' variables.
        """
        self.name = os.path.splitext(os.path.basename(filename))[0]
        mol = read_xyz(filename)
        self.atoms, self.coordinates, self.header = mol['atoms'], mol['coordinates'], mol['header']

    def write(self, filename):
        """ Write molecule file
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

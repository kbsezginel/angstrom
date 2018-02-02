"""
Molecule class for Ångström Python package.
"""
import os
from .read import read_xyz


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

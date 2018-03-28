"""
--- Ångström ---
Tests writing molecule object.
"""
from angstrom import Molecule
import filecmp
import os


benzene_xyz = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene.xyz')
benzene_atoms = ['C', 'H', 'C', 'H', 'C', 'H', 'C', 'H', 'C', 'H', 'C', 'H']
benzene_coors = [[0.0000, 1.4027, 0.0000], [0.00000, 2.4903, 0.0000],
                 [-1.2148, 0.7014, 0.0000], [-2.1567, 1.2451, 0.0000],
                 [-1.2148, -0.7014, 0.0000], [-2.1567, -1.2451, 0.0000],
                 [0.0000, -1.4027, 0.0000], [0.00000, -2.4903, 0.0000],
                 [1.2148, -0.7014, 0.0000], [2.1567, -1.2451, 0.0000],
                 [1.2148, 0.7014, 0.0000], [2.1567, 1.2451, 0.0000]]


def test_write_xyz_benzene_molecule():
    """Tests reading xyz formatted molecule file"""
    benzene = Molecule(atoms=benzene_atoms, coordinates=benzene_coors)
    test_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene_test.xyz')
    benzene.header = 'benzene'
    benzene.write(test_file)
    assert filecmp.cmp(benzene_xyz, test_file)

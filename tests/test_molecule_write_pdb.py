"""
--- Ångström ---
Tests writing molecule object.
"""
from angstrom import Molecule
import filecmp
import os
import pytest


benzene_pdb = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene.pdb')
benzene_bonds_pdb = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene_bonds.pdb')
benzene_atoms = ['C', 'H', 'C', 'H', 'C', 'H', 'C', 'H', 'C', 'H', 'C', 'H']
benzene_coors = [[0.0000, 1.4027, 0.0000], [0.00000, 2.4903, 0.0000],
                 [-1.2148, 0.7014, 0.0000], [-2.1567, 1.2451, 0.0000],
                 [-1.2148, -0.7014, 0.0000], [-2.1567, -1.2451, 0.0000],
                 [0.0000, -1.4027, 0.0000], [0.00000, -2.4903, 0.0000],
                 [1.2148, -0.7014, 0.0000], [2.1567, -1.2451, 0.0000],
                 [1.2148, 0.7014, 0.0000], [2.1567, 1.2451, 0.0000]]


# File comparison tests are OS dependent. These should only work in UNIX but not Windows.
@pytest.mark.filecmptest
def test_write_pdb_benzene_molecule():
    """
    Tests writing pdb formatted molecule file.
    File comparison tests are OS dependent, they should only work in UNIX but not Windows.
    """
    benzene = Molecule(atoms=benzene_atoms, coordinates=benzene_coors)
    test_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene_test.pdb')
    benzene.write(test_file, header='benzene')
    assert filecmp.cmp(benzene_pdb, test_file)
    os.remove(test_file)


@pytest.mark.filecmptest
def test_write_pdb_benzene_molecule_with_bonds():
    """
    Tests writing pdb formatted molecule file with bonds.
    File comparison tests are OS dependent, they should only work in UNIX but not Windows.
    """
    benzene = Molecule(atoms=benzene_atoms, coordinates=benzene_coors)
    test_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene_bonds_test.pdb')
    benzene.write(test_file, bonds=True, header='benzene')
    assert filecmp.cmp(benzene_bonds_pdb, test_file)
    os.remove(test_file)

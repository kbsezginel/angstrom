"""
--- Ångström ---
Tests Molecule rotation.
"""
from angstrom import Molecule
import numpy as np


def test_diatomic_dummy_molecule_rotation_around_global_axis():
    """ Test dummpy molecule for 90 degree rotations on global z-axis """
    mol = Molecule()
    mol.atoms = ['C'] * 2
    mol.coordinates = np.array([[1, 0, 0], [0, 1, 0]])
    mol.rotate(([0, 0, 0], [0, 0, 1]), np.pi / 2, center=False)
    assert np.allclose(mol.coordinates, [[0, 1, 0], [-1, 0, 0]])
    mol.rotate(([0, 0, 0], [0, 0, 1]), np.pi, center=False)
    assert np.allclose(mol.coordinates, [[0, -1, 0], [1, 0, 0]])


def test_diatomic_dummy_molecule_rotation_around_molecule_axis():
    """ Test dummpy molecule for 90 degree rotations on z-axis of the molecule """
    mol = Molecule()
    mol.atoms = ['C'] * 2
    mol.coordinates = np.array([[1, 0, 0], [0, 1, 0]])
    mol.rotate(([0, 0, 0], [0, 0, 1]), np.pi / 2, center=True)
    assert np.allclose(mol.coordinates, [[1, 1, 0], [0, 0, 0]])
    mol.rotate(([0, 0, 0], [0, 0, 1]), np.pi, center=True)
    assert np.allclose(mol.coordinates, [[0, 0, 0], [1, 1, 0]])

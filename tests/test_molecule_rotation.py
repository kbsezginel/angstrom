"""
--- Ångström ---
Tests Molecule rotation.
"""
from angstrom import Molecule
import numpy as np


def test_single_point_90_degrees_rotation():
    """ Test dummpy molecule for 90 degree rotations on z-axis """
    mol = Molecule()
    mol.atoms = ['C'] * 2
    mol.coordinates = np.array([[1, 0, 0], [0, 1, 0]])
    mol.rotate([0, 0, 0], [0, 0, 1], np.pi / 2)
    assert np.allclose(mol.coordinates, [[0, 1, 0], [-1, 0, 0]])
    mol.rotate([0, 0, 0], [0, 0, 1], np.pi)
    assert np.allclose(mol.coordinates, [[0, -1, 0], [1, 0, 0]])

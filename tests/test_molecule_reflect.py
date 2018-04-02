"""
--- Ångström ---
Tests Molecule reflection.
"""
from angstrom import Molecule
import numpy as np
import os


# Benzene molecule is parallel to xy plane
benzene_xyz = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene.xyz')
benzene_coors = [[0.0000, 1.4027, 0.0000], [0.00000, 2.4903, 0.0000],
                 [-1.2148, 0.7014, 0.0000], [-2.1567, 1.2451, 0.0000],
                 [-1.2148, -0.7014, 0.0000], [-2.1567, -1.2451, 0.0000],
                 [0.0000, -1.4027, 0.0000], [0.00000, -2.4903, 0.0000],
                 [1.2148, -0.7014, 0.0000], [2.1567, -1.2451, 0.0000],
                 [1.2148, 0.7014, 0.0000], [2.1567, 1.2451, 0.0000]]
benzene_bonds = [(0, 1), (0, 2), (0, 10), (2, 3), (2, 4), (4, 5),
                 (4, 6), (6, 7), (6, 8), (8, 9), (8, 10), (10, 11)]


def test_single_atom_reflection_xy_plane():
    mol = Molecule(atoms=['C'], coordinates=np.array([[0, 0, 1]]))
    mol.reflect('xy')
    assert np.allclose(mol.coordinates, [[0, 0, -1]])
    mol.reflect('xy')
    assert np.allclose(mol.coordinates, [[0, 0, 1]])
    mol.reflect('xy', translate=5)
    assert np.allclose(mol.coordinates, [[0, 0, -6]])
    mol.reflect('xy', translate=5)
    assert np.allclose(mol.coordinates, [[0, 0, 1]])


def test_benzene_reflection_should_not_change_bonding():
    mol = Molecule(read=benzene_xyz)
    mol.reflect('xy')
    mol.get_bonds()
    assert np.allclose(mol.bonds, benzene_bonds)
    mol.reflect('yz')
    mol.get_bonds()
    assert np.allclose(mol.bonds, benzene_bonds)
    mol.reflect('xz')
    mol.get_bonds()
    assert np.allclose(mol.bonds, benzene_bonds)


def test_benzene_reflection_xy_plane_should_not_change_orientation():
    mol = Molecule(read=benzene_xyz)
    mol.reflect('xy')
    assert np.allclose(mol.coordinates, benzene_coors)


def test_benzene_reflection_xz_plane_should_change_y_axis_position():
    mol = Molecule(read=benzene_xyz)
    mol.center([0, 5, 0])
    mol.reflect('xz')
    assert np.allclose(mol.get_center(), [0, -5, 0])


def test_benzene_reflection_yz_plane_should_change_x_axis_position():
    mol = Molecule(read=benzene_xyz)
    mol.center([5, 0, 0])
    mol.reflect('yz')
    assert np.allclose(mol.get_center(), [-5, 0, 0])

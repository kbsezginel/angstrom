"""
--- Ångström ---
Tests estimating molecular bonds.
"""
from angstrom import Molecule
from angstrom.molecule.bonds import get_bonds
import os


benzene_xyz = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene.xyz')


def test_atoms_too_close_should_not_be_bonded():
    atoms = ['H', 'H']
    coordinates = [[0, 0, 0], [0, 0, 0.159]]
    bonds = get_bonds(atoms, coordinates)
    assert len(bonds) == 0


def test_atoms_at_0_16_angstrom_should_be_bonded():
    atoms = ['H', 'H']
    coordinates = [[0, 0, 0], [0, 0, 0.16]]
    bonds = get_bonds(atoms, coordinates)
    assert len(bonds) == 1
    assert bonds == [(0, 1)]


def test_h_atoms_at_lt_1_09_angstrom_should_be_bonded():
    atoms = ['H', 'H']
    coordinates = [[0.0, 0.0, 0.0], [0.0, 0.0, 1.09]]
    bonds = get_bonds(atoms, coordinates)
    assert len(bonds) == 1
    assert bonds == [(0, 1)]


def test_h_atoms_at_gt_1_09_angstrom_should_not_be_bonded():
    atoms = ['H', 'H']
    coordinates = [[0.0, 0.0, 0.0], [0.0, 0.0, 1.10]]
    bonds = get_bonds(atoms, coordinates)
    assert len(bonds) == 0


def test_si_atoms_at_lt_2_77_angstrom_should_be_bonded():
    atoms = ['Si', 'Si']
    coordinates = [[0.0, 0.0, 0.0], [0.0, 0.0, 2.77]]
    bonds = get_bonds(atoms, coordinates)
    assert len(bonds) == 1
    assert bonds == [(0, 1)]


def test_si_atoms_at_gt_2_77_angstrom_should_not_be_bonded():
    atoms = ['Si', 'Si']
    coordinates = [[0.0, 0.0, 0.0], [0.0, 0.0, 2.78]]
    bonds = get_bonds(atoms, coordinates)
    assert len(bonds) == 0


def test_bond_tuples_should_be_sorted_by_atom_index():
    atoms = ['H', 'H']
    coordinates = [[0, 0, 0], [0, 0, 0.16]]
    bonds = get_bonds(atoms, coordinates)
    assert bonds == [(0, 1)]
    coordinates = [[0, 0, 0.16], [0, 0, 0]]
    bonds = get_bonds(atoms, coordinates)
    assert bonds == [(0, 1)]


def test_ethane_should_have_seven_bonds():
    atoms = ['H', 'C', 'H', 'H', 'C', 'H', 'H', 'H']
    coordinates = [[ 1.185080, -0.003838,  0.987524],
                   [ 0.751621, -0.022441, -0.020839],
                   [ 1.166929,  0.833015, -0.569312],
                   [ 1.115519, -0.932892, -0.514525],
                   [-0.751587,  0.022496,  0.020891],
                   [-1.166882, -0.833372,  0.568699],
                   [-1.115691,  0.932608,  0.515082],
                   [-1.184988,  0.004424, -0.987522]]
    bonds = get_bonds(atoms, coordinates)
    assert len(bonds) == 7
    expected_bonds = [(0, 1),
                      (1, 2),
                      (1, 3),
                      (1, 4),
                      (4, 5),
                      (4, 6),
                      (4, 7)]
    assert bonds == expected_bonds


def test_benzene_read_and_get_bonds():
    benzene = Molecule(read=benzene_xyz)
    benzene.get_bonds()
    assert len(benzene.bonds) == 12
    expected_bonds = [(0, 1),
                      (0, 2),
                      (0, 10),
                      (2, 3),
                      (2, 4),
                      (4, 5),
                      (4, 6),
                      (6, 7),
                      (6, 8),
                      (8, 9),
                      (8, 10),
                      (10, 11)]
    assert benzene.bonds == expected_bonds

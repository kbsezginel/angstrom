"""
--- Ångström ---
Tests estimating molecular bonds.
"""
from angstrom.molecule.bonds import get_bonds


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

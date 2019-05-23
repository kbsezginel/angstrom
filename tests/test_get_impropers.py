"""
--- Ångström ---
Tests estimating molecular improper torsions.
"""
from angstrom.molecule.impropers import get_impropers


def test_triangle_molecule_should_have_no_impropers():
    bonds = [(0, 1), (0, 2), (1, 2)]
    assert get_impropers(bonds) == []


def test_four_atom_linear_molecule_should_have_no_impropers():
    bonds = [(0, 1), (1, 2), (2, 3)]
    assert get_impropers(bonds) == []


def test_different_order_of_bonds_should_return_same_impropers():
    bonds = [(0, 1), (0, 2), (0, 3)]
    assert get_impropers(bonds) == [(1, 0, 2, 3), (2, 0, 1, 3), (3, 0, 1, 2)]
    bonds = [(0, 3), (0, 2), (0, 1)]
    assert get_impropers(bonds) == [(1, 0, 2, 3), (2, 0, 1, 3), (3, 0, 1, 2)]


def test_square_molecule_should_have_no_impropers():
    bonds = [(0, 1), (1, 2), (2, 3), (0, 3)]
    assert get_impropers(bonds) == []


def test_tetrahedral_molecule_should_have_three_impropers():
    bonds = [(0, 3), (1, 3), (2, 3)]
    assert get_impropers(bonds) == [(0, 3, 1, 2), (1, 3, 0, 2), (2, 3, 0, 1)]


def test_square_planar_molecule_should_have_twelve_impropers():
    bonds = [(0, 1), (0, 2), (0, 3), (0, 4)]
    assert get_impropers(bonds) == [(1, 0, 2, 3), (1, 0, 2, 4), (1, 0, 3, 4),
                                    (2, 0, 1, 3), (2, 0, 1, 4), (2, 0, 3, 4),
                                    (3, 0, 1, 2), (3, 0, 1, 4), (3, 0, 2, 4),
                                    (4, 0, 1, 2), (4, 0, 1, 3), (4, 0, 2, 3)]


def test_octahedral_molecule_should_have_eighteen_impropers():
    bonds = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]
    assert len(get_impropers(bonds)) == 60

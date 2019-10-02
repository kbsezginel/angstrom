"""
--- Ångström ---
Tests bond, angle, dihedral estimation for Molecule class.
"""
from angstrom import Molecule
import os


benzene_xyz = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene.xyz')
ethane = Molecule(atoms=['H', 'C', 'H', 'H', 'C', 'H', 'H', 'H'],
                  coordinates = [[ 1.185080, -0.003838,  0.987524],
                                 [ 0.751621, -0.022441, -0.020839],
                                 [ 1.166929,  0.833015, -0.569312],
                                 [ 1.115519, -0.932892, -0.514525],
                                 [-0.751587,  0.022496,  0.020891],
                                 [-1.166882, -0.833372,  0.568699],
                                 [-1.115691,  0.932608,  0.515082],
                                 [-1.184988,  0.004424, -0.987522]])


def test_ethane_should_have_seven_bonds():
    expected_bonds = [(0, 1),
                      (1, 2),
                      (1, 3),
                      (1, 4),
                      (4, 5),
                      (4, 6),
                      (4, 7)]
    ethane.get_bonds()
    assert ethane.bonds == expected_bonds

def test_ethane_should_have_twelve_angles():
    expected_angles = [(0, 1, 2), (0, 1, 3), (0, 1, 4),
                       (1, 4, 5), (1, 4, 6), (1, 4, 7),
                       (2, 1, 3), (2, 1, 4), (3, 1, 4),
                       (5, 4, 6), (5, 4, 7), (6, 4, 7)]
    ethane.get_angles()
    assert ethane.angles == expected_angles

def test_ethane_should_have_nine_dihedrals():
    expected_dihedrals = [(0, 1, 4, 5), (0, 1, 4, 6), (0, 1, 4, 7),
                          (2, 1, 4, 5), (2, 1, 4, 6), (2, 1, 4, 7),
                          (3, 1, 4, 5), (3, 1, 4, 6), (3, 1, 4, 7)]
    ethane.get_dihedrals()
    assert ethane.dihedrals == expected_dihedrals

def test_ethane_should_have_twenty_four_impropers():
    expected_impropers = [(0, 1, 2, 3), (0, 1, 2, 4), (0, 1, 3, 4), (1, 4, 5, 6),
                          (1, 4, 5, 7), (1, 4, 6, 7), (2, 1, 0, 3), (2, 1, 0, 4),
                          (2, 1, 3, 4), (3, 1, 0, 2), (3, 1, 0, 4), (3, 1, 2, 4),
                          (4, 1, 0, 2), (4, 1, 0, 3), (4, 1, 2, 3), (5, 4, 1, 6),
                          (5, 4, 1, 7), (5, 4, 6, 7), (6, 4, 1, 5), (6, 4, 1, 7),
                          (6, 4, 5, 7), (7, 4, 1, 5), (7, 4, 1, 6), (7, 4, 5, 6)]
    ethane.get_impropers()
    assert ethane.impropers == expected_impropers

def test_benzene_read_and_get_topology():
    benzene = Molecule(read=benzene_xyz)
    benzene.get_topology()

    expected_bonds = [(0, 1), (0, 2), (0, 10), (2, 3), (2, 4), (4, 5),
                      (4, 6), (6, 7), (6, 8), (8, 9), (8, 10), (10, 11)]
    assert benzene.bonds == expected_bonds

    expected_angles = [(0, 2, 3), (0, 2, 4), (0, 10, 8), (0, 10, 11), (1, 0, 2), (1, 0, 10),
                       (2, 0, 10), (2, 4, 5), (2, 4, 6), (3, 2, 4), (4, 6, 7), (4, 6, 8),
                       (5, 4, 6), (6, 8, 9), (6, 8, 10), (7, 6, 8), (8, 10, 11), (9, 8, 10)]
    assert benzene.angles == expected_angles

    expected_dihedrals = [(0, 2, 4, 5), (0, 2, 4, 6), (0, 8, 10, 6), (0, 8, 10, 9),
                          (1, 0, 2, 3), (1, 0, 2, 4), (1, 0, 10, 8), (1, 0, 10, 11),
                          (2, 0, 10, 8), (2, 0, 10, 11), (2, 4, 6, 7), (2, 4, 6, 8),
                          (3, 0, 2, 10), (3, 2, 4, 5), (3, 2, 4, 6), (4, 0, 2, 10),
                          (4, 6, 8, 9), (4, 6, 8, 10), (5, 4, 6, 7), (5, 4, 6, 8),
                          (6, 8, 10, 11), (7, 6, 8, 9), (7, 6, 8, 10), (9, 8, 10, 11)]
    assert benzene.dihedrals == expected_dihedrals

    expected_impropers = [(0, 2, 3, 4), (0, 10, 8, 11), (1, 0, 2, 10), (2, 0, 1, 10),
                          (2, 4, 5, 6), (3, 2, 0, 4), (4, 2, 0, 3), (4, 6, 7, 8),
                          (5, 4, 2, 6), (6, 4, 2, 5), (6, 8, 9, 10), (7, 6, 4, 8),
                          (8, 6, 4, 7), (8, 10, 0, 11), (9, 8, 6, 10), (10, 0, 1, 2),
                          (10, 8, 6, 9), (11, 10, 0, 8)]
    assert benzene.impropers == expected_impropers

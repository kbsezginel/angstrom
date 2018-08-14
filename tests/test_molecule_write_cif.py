"""
--- Ångström ---
Tests writing molecule object.
"""
from angstrom import Molecule
import filecmp
import os
import pytest


piyzaz_cif = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'piyzaz.cif')
piyzaz_cell_parameters = [8.9950, 8.9950, 8.9950, 60, 60, 60]
piyzaz_atoms = ['Cd', 'Cd', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C']
piyzaz_coors = [[6.746250, 6.491582, 4.590242],
                [11.243750, 3.894949, 2.754145],
                [6.746250, 8.536898, 3.867113],
                [8.517545, 5.468924, 3.867113],
                [4.974955, 5.468924, 3.867113],
                [6.746250, 6.491582, 6.759627],
                [9.472455, 4.917607, 3.477273],
                [11.243750, 1.849634, 3.477273],
                [13.015045, 4.917607, 3.477273],
                [11.243750, 3.894949, 0.584760]]


@pytest.mark.filecmptest
def test_write_cif_PIYZAZ():
    """
    Tests writing cif formatted molecule file
    File comparison tests are OS dependent, they should only work in UNIX but not Windows.
    """
    piyzaz = Molecule(atoms=piyzaz_atoms, coordinates=piyzaz_coors)
    test_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'piyzaz_test.cif')
    piyzaz.write(test_file, cell=piyzaz_cell_parameters, header='piyzaz')
    assert filecmp.cmp(piyzaz_cif, test_file)
    os.remove(test_file)

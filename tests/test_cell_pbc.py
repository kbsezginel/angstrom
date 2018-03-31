"""
--- Ångström ---
Tests cell periodic boundary conditions calculations.
"""
from angstrom.molecule import Cell
import numpy as np


def test_cubic_unit_cell_pbc():
    cell = Cell([10, 10, 10, 90.0, 90.0, 90.0])
    assert np.allclose([2, 2, 2], cell.car2frac([20, 20, 20]))
    assert np.allclose([20, 20, 20], cell.frac2car([2, 2, 2]))

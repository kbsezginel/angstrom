"""
--- Ångström ---
Tests cell edges calculation.
"""
from angstrom.molecule import Cell
import numpy as np


def test_cubic_unit_cell_edges_calculation():
    a, b, c = 5, 5, 5
    expected_edges = [[[a, 0, 0], [0, 0, 0]], [[0, b, 0], [0, 0, 0]], [[0, 0, c], [0, 0, 0]],
                      [[a, b, 0], [a, 0, 0]], [[a, 0, c], [a, 0, 0]], [[a, b, 0], [0, b, 0]],
                      [[0, b, c], [0, b, 0]], [[0, b, c], [0, 0, c]], [[a, 0, c], [0, 0, c]],
                      [[a, b, c], [a, b, 0]], [[a, b, c], [0, b, c]], [[a, b, c], [a, 0, c]]]
    cell = Cell([a, b, c, 90.0, 90.0, 90.0])
    assert np.allclose(cell.edges, expected_edges)

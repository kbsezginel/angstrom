"""
--- Ångström ---
Tests cell vertices calculation.
"""
from angstrom.molecule import Cell
import numpy as np


def test_cubic_unit_cell_should_return_cubic_vertices_without_vector_calculation():
    expected_vertices = [[0.00000, 0.00000, 0.00000],
                         [18.6400, 0.00000, 0.00000],
                         [0.00000, 18.6400, 0.00000],
                         [0.00000, 0.00000, 18.6400],
                         [18.6400, 18.6400, 0.00000],
                         [0.00000, 18.6400, 18.6400],
                         [18.6400, 0.00000, 18.6400],
                         [18.6400, 18.6400, 18.6400]]
    cell = Cell([18.6400, 18.6400, 18.6400, 90.0, 90.0, 90.0])
    cell.calculate_vertices()
    assert np.allclose(cell.vertices, expected_vertices)


def test_cubic_unit_cell_should_return_cubic_vertices_with_vector_calculation():
    expected_vertices = [[0.0000, 0.0000, 0.0000],
                         [8.4000, 0.0000, 0.0000],
                         [0.0000, 8.4000, 0.0000],
                         [0.0000, 0.0000, 8.4000],
                         [8.4000, 8.4000, 0.0000],
                         [0.0000, 8.4000, 8.4000],
                         [8.4000, 0.0000, 8.4000],
                         [8.4000, 8.4000, 8.4000]]
    cell = Cell([8.4000, 8.4000, 8.4000, 90.0, 90.0, 90.0])
    cell.calculate_vectors()
    cell.calculate_vertices()
    assert np.allclose(cell.vertices, expected_vertices)

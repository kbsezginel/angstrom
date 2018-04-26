"""
--- Ångström ---
Tests Plane grid generation.
"""
import numpy as np
from angstrom.geometry import Plane


def test_number_of_grid_points_for_different_grid_sizes_and_grid_spaces():
    sizes, spaces = np.arange(1, 6), np.arange(0.2, 1.2, 0.2)
    plane = Plane('xy')
    for gsize, gspace in zip(sizes, spaces):
        assert len(plane.grid(gsize, gspace)) == (np.ceil(gsize / gspace) + 1) ** 2

    plane = Plane('yz', size=5)
    for gsize, gspace in zip(sizes, spaces):
        assert len(plane.grid(gsize, gspace)) == (np.ceil(gsize / gspace) + 1) ** 2


def test_grids_from_planes_with_different_size_match_given_correct_size_and_spacing():
    p1, p2, p3 = [0, 0, 0], [0, 5, 0], [0, 5, 5]
    plane = Plane(p1, p2, p3)

    plane_yz = Plane('yz', size=1)
    # The grid spacing for the first and second planes are 5 and 1, respectively
    assert np.allclose(plane.grid(1, 1), plane_yz.grid(5, 5))
    assert np.allclose(plane.grid(1, .2), plane_yz.grid(5, 1))

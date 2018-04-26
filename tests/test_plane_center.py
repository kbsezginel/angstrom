"""
--- Ångström ---
Tests Plane center calculation.
"""
import numpy as np
from angstrom.geometry import Plane


def test_xy_and_yx_plane_center():
    for p in range(1, 6):
        plane = Plane('xy', size=p)
        assert np.allclose(plane.get_center(), [p / 2, p / 2, 0])
        plane = Plane('yx', size=p)
        assert np.allclose(plane.get_center(), [p / 2, p / 2, 0])


def test_yz_and_zy_plane_center():
    for p in range(1, 6):
        plane = Plane('yz', size=p)
        assert np.allclose(plane.get_center(), [0, p / 2, p / 2])
        plane = Plane('zy', size=p)
        assert np.allclose(plane.get_center(), [0, p / 2, p / 2])


def test_zx_and_xz_plane_center():
    for p in range(1, 6):
        plane = Plane('zx', size=p)
        assert np.allclose(plane.get_center(), [p / 2, 0, p / 2])
        plane = Plane('xz', size=p)
        assert np.allclose(plane.get_center(), [p / 2, 0, p / 2])

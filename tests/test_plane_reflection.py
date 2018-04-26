"""
--- Ångström ---
Tests Plane reflection.
"""
from angstrom.geometry import Plane
import numpy as np


def test_xy_and_yx_plane_reflection():
    xy_plane = Plane('xy')
    yx_plane = Plane('yx')
    for p in range(-3, 4):
        assert np.allclose(xy_plane.reflect([0, 0, p]), [0, 0, -p])
        assert np.allclose(yx_plane.reflect([0, 0, p]), [0, 0, -p])


def test_xz_and_zx_plane_reflection():
    xz_plane = Plane('xz')
    zx_plane = Plane('zx')
    for p in range(-3, 4):
        assert np.allclose(xz_plane.reflect([0, p, 0]), [0, -p, 0])
        assert np.allclose(zx_plane.reflect([0, p, 0]), [0, -p, 0])


def test_yz_and_zy_plane_reflection():
    yz_plane = Plane('yz')
    zy_plane = Plane('zy')
    for p in range(-3, 4):
        assert np.allclose(yz_plane.reflect([p, 0, 0]), [-p, 0, 0])
        assert np.allclose(zy_plane.reflect([p, 0, 0]), [-p, 0, 0])

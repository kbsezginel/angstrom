"""
--- Ångström ---
Tests Quaternion rotations.
"""
from angstrom.geometry import Quaternion
import numpy as np


def test_single_point_90_degrees_rotation():
    """
    Test 90 degree rotation around a single point.
    """
    Q = Quaternion([0, 1, 1, 1])
    # Rotate (1, 0, 0) around z-axis first counter-clockwise then clockwise
    assert np.allclose(Q.rotation([1, 0, 0], ([0, 0, 0], [0, 0, 1]), np.pi / 2).xyz(), [0, 1, 0])
    assert np.allclose(Q.rotation([1, 0, 0], ([0, 0, 0], [0, 0, 1]), -np.pi / 2).xyz(), [0, -1, 0])
    # Rotate (0, 1, 0) around x-axis first counter-clockwise then clockwise
    assert np.allclose(Q.rotation([0, 1, 0], ([0, 0, 0], [1, 0, 0]), np.pi / 2).xyz(), [0, 0, 1])
    assert np.allclose(Q.rotation([0, 1, 0], ([0, 0, 0], [1, 0, 0]), -np.pi / 2).xyz(), [0, 0, -1])
    # Rotate (0, 0, 1) around y-axis first counter-clockwise then clockwise
    assert np.allclose(Q.rotation([0, 0, 1], ([0, 0, 0], [0, 1, 0]), np.pi / 2).xyz(), [1, 0, 0])
    assert np.allclose(Q.rotation([0, 0, 1], ([0, 0, 0], [0, 1, 0]), -np.pi / 2).xyz(), [-1, 0, 0])


def test_primary_axes_rotations():
    """
    Tests rotation of a random point around primary axes by a random angle.
    """
    Q = Quaternion([0, 1, 1, 1])
    # Rotate (1, 0, 0) around z-axis first counter-clockwise then clockwise
    point = [np.random.normal(), np.random.normal(), np.random.normal()]
    x_axis = ([0, 0, 0], [1, 0, 0])
    y_axis = ([0, 0, 0], [0, 1, 0])
    z_axis = ([0, 0, 0], [0, 0, 1])
    angle = np.pi * np.random.normal()
    assert np.allclose(Q.rotation(point, x_axis, angle).xyz(), Q.rotation(point, 'x', angle).xyz())
    assert np.allclose(Q.rotation(point, y_axis, angle).xyz(), Q.rotation(point, 'y', angle).xyz())
    assert np.allclose(Q.rotation(point, z_axis, angle).xyz(), Q.rotation(point, 'z', angle).xyz())

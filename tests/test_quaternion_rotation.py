"""
--- Ångström ---
Tests Quaternion rotations.
"""
from angstrom.geometry import Quaternion
import numpy as np


def test_single_point_90_degrees_rotation():
    """ """
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

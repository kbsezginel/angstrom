"""
--- Ångström ---
Tests aligning vectors.
"""
from angstrom.geometry import align_vectors
import numpy as np
import pytest


def test_x_and_y_unit_vectors_alignment():
    """ Tests (1, 0, 0) and (0, 1, 0) vectors alignment including direction and normalization """
    # Tests aligning x and y unit vectors with respect to y
    v1, v2 = np.array([1, 0, 0]), np.array([0, 1, 0])
    alignment = align_vectors(v1, v2)
    assert np.allclose(alignment['axis'], [0, 0, 1])
    assert np.isclose(alignment['angle'], np.pi / 2)

    # Tests aligning x and y unit vectors with respect to x
    v1, v2 = np.array([1, 0, 0]), np.array([0, 1, 0])
    alignment = align_vectors(v2, v1)
    assert np.allclose(alignment['axis'], [0, 0, -1])
    assert np.isclose(alignment['angle'], np.pi / 2)

    # Tests aligning x and y unit vectors with respect to y without normalization
    v1, v2 = np.array([1, 0, 0]), np.array([0, 1, 0])
    alignment = align_vectors(v1, v2, norm=False)
    assert np.allclose(alignment['axis'], [0, 0, 1])
    assert np.isclose(alignment['angle'], np.pi / 2)


def test_aligning_parallel_vectors_should_raise_warning_and_give_zero_degrees():
    """ Tests aligning parallel vectors which should return an angle of 0 radians """
    v1, v2 = np.array([1, 1, 1]), np.array([-2, -2, -2])
    alignment = align_vectors(v1, v2)
    pytest.warns(RuntimeWarning, "align_vectors(v1, v2)")
    assert np.allclose(alignment['axis'], [0, 0, 0])
    assert np.isclose(alignment['angle'], 0)

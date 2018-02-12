"""
--- Ångström ---
Tests aligning molecules.
"""
from angstrom import Molecule
from angstrom.geometry import align_vectors
import numpy as np
import os

benzene_xyz = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene.xyz')


def test_benzene_alignment():
    """ Tests alinging benzene from xy plane to xz plane """
    benzene = Molecule(read=benzene_xyz)
    v_align = [0, 0, 1]
    v_benzene = benzene.coordinates[0] - benzene.coordinates[6]
    benzene.align(v_benzene, v_align)
    # Check if the benzene vector is parallel to z-axis
    assert np.allclose(np.cross(benzene.coordinates[0] - benzene.coordinates[6], v_align), [0, 0, 0])

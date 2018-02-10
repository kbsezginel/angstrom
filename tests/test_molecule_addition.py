"""
--- Ångström ---
Tests molecule addition.
"""
from angstrom import Molecule
import numpy as np
import os

benzene_xyz = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene.xyz')


def test_benzene_addition():
    """Tests molecular addition of two benzenes"""
    benzene = Molecule(read=benzene_xyz)
    benzene2 = benzene + benzene
    assert len(benzene2.atoms) == 2 * len(benzene.atoms)
    assert len(benzene2.coordinates) == 2 * len(benzene.coordinates)
    assert np.allclose(benzene2.coordinates[:12, :], benzene.coordinates)
    assert np.allclose(benzene2.coordinates[12:, :], benzene.coordinates)
    for atom, ref_atom in zip(benzene2.atoms[12:], benzene.atoms):
        assert atom == ref_atom
    for atom, ref_atom in zip(benzene2.atoms[:12], benzene.atoms):
        assert atom == ref_atom
    assert benzene2.name == 'benzene+benzene'

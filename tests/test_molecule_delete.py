"""
--- Ångström ---
Tests molecule delete.
"""
from angstrom import Molecule
import os

benzene_xyz = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene.xyz')


def test_benzene_delete():
    """Tests deleting atoms from benzene molecule"""
    benzene = Molecule(read=benzene_xyz)
    benzene.delete([0, 2, 4, 6, 8, 10])
    assert len(benzene.atoms) == 6
    assert all([a == 'H' for a in benzene.atoms])

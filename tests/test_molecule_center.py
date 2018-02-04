"""
--- Ångström ---
Tests reading molecule object.
"""
from angstrom import Molecule
from angstrom.geometry import get_molecule_center
import numpy as np
import os

benzene_xyz = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene.xyz')


def test_get_molecule_center_benzene():
    """Tests molecule center for benzene"""
    benzene = Molecule(read=benzene_xyz)
    benzene_com = benzene.get_center()
    benzene_cog = benzene.get_center(mass=False)
    assert np.allclose(benzene_com, [0, 0, 0])
    assert np.allclose(benzene_com, benzene_cog)

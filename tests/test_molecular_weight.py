"""
--- Ångström ---
Tests aligning molecules.
"""
from angstrom import Molecule
import numpy as np
import os

benzene_xyz = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene.xyz')


def test_benzene_molecular_weight():
    """ Tests molecular weight calculation for benzene molecule """
    benzene = Molecule(read=benzene_xyz)
    mw = benzene.get_molecular_weight()
    assert np.isclose(mw, 78.11, atol=0.01)


def test_caffeine_molecular_weight():
    """ Testing impotant stuff here """
    caffeine = Molecule(atoms=['C'] * 8 + ['H'] * 10 + ['N'] * 4 + ['O'] * 2, coordinates=[])
    mw = caffeine.get_molecular_weight()
    assert np.isclose(mw, 194.194, atol=0.01)

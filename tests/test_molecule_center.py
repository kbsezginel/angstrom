"""
--- Ångström ---
Tests calculating molecular center for given molecule.
"""
from angstrom import Molecule
from angstrom.geometry import get_molecule_center
import numpy as np
import os

benzene_xyz = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene.xyz')


def test_molecule_center_calculation_of_benzene():
    """Tests molecule center for benzene"""
    benzene = Molecule(read=benzene_xyz)
    benzene_com = benzene.get_center()              # Center of mass
    benzene_cog = benzene.get_center(mass=False)    # Geometric center
    assert np.allclose(get_molecule_center(benzene.atoms, benzene.coordinates), [0, 0, 0])
    assert np.allclose(benzene_com, [0, 0, 0])
    assert np.allclose(benzene_com, benzene_cog)


def test_centering_benzene_molecule_to_given_coordinates():
    """Tests molecule center for benzene"""
    benzene = Molecule(read=benzene_xyz)
    benzene.center([5, 0, -5])
    assert np.allclose(benzene.get_center(), [5, 0, -5])
    benzene.center()
    assert np.allclose(benzene.get_center(), [0, 0, 0])
    benzene.translate([0, 0, 7])
    assert np.allclose(benzene.get_center(), [0, 0, 7])
    benzene.rotate(([0, 0, 0], [0, 1, 0]), np.pi / 2)
    assert np.allclose(benzene.get_center(), [7, 0, 0])
    benzene.rotate(([0, 0, 0], [0, 1, 0]), np.pi / 2, center=True)
    assert np.allclose(benzene.get_center(), [7, 0, 0])

"""
--- Ångström ---
Tests reading molecule object.
"""
from angstrom import Molecule
import numpy as np
import os


benzene_xyz = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene.xyz')
benzene_atoms = ['C', 'H', 'C', 'H', 'C', 'H', 'C', 'H', 'C', 'H', 'C', 'H']
benzene_coors = [[0.0000, 1.4027, 0.0000], [0.00000, 2.4903, 0.0000],
                 [-1.2148, 0.7014, 0.0000], [-2.1567, 1.2451, 0.0000],
                 [-1.2148, -0.7014, 0.0000], [-2.1567, -1.2451, 0.0000],
                 [0.0000, -1.4027, 0.0000], [0.00000, -2.4903, 0.0000],
                 [1.2148, -0.7014, 0.0000], [2.1567, -1.2451, 0.0000],
                 [1.2148, 0.7014, 0.0000], [2.1567, 1.2451, 0.0000]]


def test_read_xyz_benzene_molecule():
    """Tests reading xyz formatted molecule file"""
    benzene = Molecule(read=benzene_xyz)
    assert len(benzene) == 12
    assert len(benzene.atoms) == 12
    assert len(benzene.coordinates) == 12
    assert benzene.header == 'benzene'
    for atom, ref_atom in zip(benzene.atoms, benzene_atoms):
        assert atom == ref_atom
    assert np.allclose(benzene.coordinates, benzene_coors)

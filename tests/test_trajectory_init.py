"""
--- Ångström ---
Tests reading xyz trajectory.
"""
from angstrom import Trajectory, Molecule
import numpy as np
import os


benzene_xyz = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene.xyz')


def test_trajectory_from_molecule():
    """Tests converting Molecule to Trajectory object"""
    benzene = Molecule(read=benzene_xyz)
    benzene_traj = Trajectory(molecule=benzene)
    assert len(benzene_traj) == 1
    assert benzene_traj.name == 'benzene'
    assert np.shape(benzene_traj.coordinates) == (1, 12, 3)
    assert np.shape(benzene_traj.atoms) == (1, 12)

    # Test atom names are read correctly
    for frame in benzene_traj:
        assert len(frame.coordinates) == 12
        for atom, ref_atom in zip(frame.atoms, benzene.atoms):
            assert atom == ref_atom

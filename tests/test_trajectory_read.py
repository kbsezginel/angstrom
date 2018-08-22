"""
--- Ångström ---
Tests reading xyz trajectory.
"""
from angstrom import Trajectory
import numpy as np
import os

benzene_traj_x = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene-traj-x.xyz')
benzene_atoms = ['C', 'H', 'C', 'H', 'C', 'H', 'C', 'H', 'C', 'H', 'C', 'H']


def test_read_xyz_benzene_trajectory():
    """Tests reading xyz formatted trajectory"""
    benzene_traj = Trajectory(read=benzene_traj_x)
    assert len(benzene_traj) == 50
    assert benzene_traj.name == 'benzene-traj-x'
    assert np.shape(benzene_traj.coordinates) == (50, 12, 3)
    assert np.shape(benzene_traj.atoms) == (50, 12)
    assert np.shape(benzene_traj.headers) == (50,)

    # Test headers are read correctly
    for idx, header in enumerate(benzene_traj.headers):
        assert header == 'angstrom - %i' % idx

    # Test atom names are read correctly
    for frame in benzene_traj:
        assert len(frame.coordinates) == 12
        for atom, ref_atom in zip(frame.atoms, benzene_atoms):
            assert atom == ref_atom

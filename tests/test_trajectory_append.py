"""
--- Ångström ---
Tests appending molecule to trajectory.
"""
import os
from angstrom import Trajectory, Molecule


benzene_traj_x = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene-traj-x.xyz')
benzene_xyz = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene.xyz')


def test_trajectory_append_molecule():
    """Tests appending molecule to trajectory"""
    benzene_traj = Trajectory(read=benzene_traj_x)
    n_frames = len(benzene_traj)
    benzene_mol = Molecule(read=benzene_xyz)
    benzene_traj.append(benzene_mol)
    assert len(benzene_traj) == n_frames + 1
    assert benzene_traj.atoms.shape[0] == n_frames + 1
    assert benzene_traj.atoms.shape[1] == len(benzene_mol)
    assert benzene_traj.coordinates.shape[0] == n_frames + 1
    assert benzene_traj.coordinates.shape[1] == len(benzene_mol)

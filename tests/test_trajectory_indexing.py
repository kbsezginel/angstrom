"""
--- Ångström ---
Tests indexing a Trajectory.
"""
from angstrom import Trajectory, Molecule
import numpy as np
import os

benzene_traj_x = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene-traj-x.xyz')


def test_trajectory_indexing_atoms_and_coordinates():
    """Tests Trajectory indexing atoms, coordinates and class type."""
    benzene_traj = Trajectory(read=benzene_traj_x)

    for frame_idx, benzene_frame in enumerate(benzene_traj):
        assert np.allclose(benzene_traj[frame_idx].coordinates, benzene_traj.coordinates[frame_idx])
        for atom, ref_atom in zip(benzene_traj[frame_idx].atoms, benzene_traj.atoms[frame_idx]):
            assert atom == ref_atom
        assert isinstance(benzene_traj[frame_idx], Molecule)
        assert len(benzene_traj[frame_idx].atoms) == 12
        assert len(benzene_traj[frame_idx].coordinates) == 12


def test_trajectory_indexing_center_of_mass():
    """Tests calculating center of mass for each frame separately by indexing the Trajectory."""
    benzene_traj = Trajectory(read=benzene_traj_x)
    benzene_coms = benzene_traj.get_center()
    for frame_idx, benzene_frame in enumerate(benzene_traj):
        assert np.allclose(benzene_traj[frame_idx].get_center(), benzene_coms[frame_idx])


def test_trajectory_slicing_with_random_integers():
    """Tests Trajectory sllicing."""
    benzene_traj = Trajectory(read=benzene_traj_x)
    n_atoms = len(benzene_traj)
    # Try 5 random slicing
    for i in range(5):
        start = np.random.randint(n_atoms)
        stop = np.random.randint(n_atoms)
        step = np.random.randint(n_atoms)
        benzene_slice = benzene_traj[start:stop:step]
        indices = range(start, stop, step)
        assert len(indices) == len(benzene_slice)
        if len(indices) == 0:
            assert type(benzene_slice) == list
        else:
            assert type(benzene_slice) == Trajectory

"""
--- Ångström ---
Tests iterating over a Trajectory.
"""
from angstrom import Trajectory, Molecule
import numpy as np
import os

benzene_traj_x = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene-traj-x.xyz')


def test_trajectory_iteration_atoms_and_coordinates():
    """Tests Trajectory iteration atoms, coordinates and class type."""
    benzene_traj = Trajectory(read=benzene_traj_x)

    for frame_idx, benzene_frame in enumerate(benzene_traj):
        assert np.allclose(benzene_frame.coordinates, benzene_traj.coordinates[frame_idx])
        for atom, ref_atom in zip(benzene_frame.atoms, benzene_traj.atoms[frame_idx]):
            assert atom == ref_atom
        assert isinstance(benzene_frame, Molecule)
        assert len(benzene_frame.atoms) == 12
        assert len(benzene_frame.coordinates) == 12
    assert frame_idx == len(benzene_traj.atoms) - 1


def test_trajectory_iteration_center_of_mass():
    """Tests calculating center of mass for each frame separately by looping over the Trajectory."""
    benzene_traj = Trajectory(read=benzene_traj_x)
    benzene_coms = benzene_traj.get_center()
    for frame_idx, benzene_frame in enumerate(benzene_traj):
        assert np.allclose(benzene_frame.get_center(), benzene_coms[frame_idx])

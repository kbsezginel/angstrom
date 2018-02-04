"""
--- Ångström ---
Tests calculating molecular center for a trajectory.
"""
from angstrom import Trajectory
from angstrom.geometry import get_molecule_center
import numpy as np
import os

benzene_traj_x = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene-traj-x.xyz')


def test_trajectory_center_of_benzene_moving_linearly_in_x():
    """Tests molecular center calculation for benzene moving linearly in +x direction"""
    benzene = Trajectory(read=benzene_traj_x)
    benzene_coms = benzene.get_center()
    benzene_cogs = benzene.get_center(mass=False)
    # Make an array of initial positions for each frame and increase all x coordinates by 1
    benzene_coms_ref = np.array([[3, 3, 3]] * len(benzene.atoms))
    benzene_coms_ref[:, 0] = np.arange(3, len(benzene.atoms) + 3)
    assert np.allclose(benzene_coms[0], [3, 3, 3])
    assert np.allclose(benzene_coms, benzene_coms_ref)
    assert np.allclose(benzene_cogs, benzene_coms_ref)

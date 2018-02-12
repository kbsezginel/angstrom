"""
--- Ångström ---
Tests calculating mean squared displacement for a trajectory.
"""
from angstrom import Trajectory
import os

benzene_traj_x = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene-traj-x.xyz')


def test_trajectory_msd_of_benzene_moving_linearly_in_x():
    """Tests MSD calculation for benzene moving linearly in +x direction"""
    benzene = Trajectory(read=benzene_traj_x)
    assert benzene.get_msd(benzene.coordinates[:, 0, 0]) == 808.5
    assert benzene.get_msd(benzene.coordinates[:, 0, 1]) == 0
    assert benzene.get_msd(benzene.coordinates[:, 0, 2]) == 0

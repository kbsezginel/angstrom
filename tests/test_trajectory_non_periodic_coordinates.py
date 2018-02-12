"""
--- Ångström ---
Tests converting periodic trajectory coordinates to non-periodic coordinates.
"""
from angstrom import Trajectory
import numpy as np
import os

benzene_traj_p_x = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene-traj-p-x.xyz')
benzene_traj_nonp_x = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene-traj-nonp-x.xyz')


def test_converting_periodic_trajectory_of_benzene_moving_linearly_in_x():
    """Tests converting periodic trajectory of benzene in a cubic box (20 Å) moving linearly in +x direction"""
    benzene_p = Trajectory(read=benzene_traj_p_x)
    np_coor = benzene_p.non_periodic_coordinates([20, 20, 20])
    benzene_nonp = Trajectory(read=benzene_traj_nonp_x)
    assert np.allclose(np_coor, benzene_nonp.coordinates)

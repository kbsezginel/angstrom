"""
--- Ångström ---
Geometric operations for Ångström Python package.
"""
import warnings
import numpy as np
import periodictable


def get_molecule_center(atoms, coordinates, mass=True):
    """ Calculate center of mass or geometric center for given coordinates and atom names of a molecule.

    Parameters
    ----------
    atoms: ndarray
        List of element names
    coordinates: ndarray
        List of coordinates (2D list)
    mass: bool
        Use atomic masses (True) or calculate geometric center (False)

    Returns
    -------
    ndarray
        Center coordinate
    """
    if mass:
        masses = np.array([periodictable.elements.symbol(atom).mass for atom in atoms])
    else:
        masses = np.ones(len(atoms))
    total_mass = masses.sum()
    x_cm = (masses * coordinates[:, 0]).sum() / total_mass
    y_cm = (masses * coordinates[:, 1]).sum() / total_mass
    z_cm = (masses * coordinates[:, 2]).sum() / total_mass
    return np.array([x_cm, y_cm, z_cm])


def align_vectors(v1, v2, norm=True):
    """ Calculates the rotation axis and angle to align two vectors (v1 to v2).

    Parameters
    ----------
    v1: ndarray
        Vector 1
    v2: ndarray
        Vector 2
    norm: bool
        Normalize vectors (default: True)

    Returns
    -------
    dict
        Rotation axis and angle for aligning vectors

    Warns
    -----
    RuntimeWarning
        If v1 and v2 are already aligned (parallel). In this case the angle will be returned 0.
    """
    if norm:
        v1 = np.array(v1) / np.linalg.norm(v1)
        v2 = np.array(v2) / np.linalg.norm(v2)
    rotation_axis = np.cross(v1, v2)
    d = np.dot(v1, v2)
    angle = np.arccos(d)
    if np.isnan(angle):
        angle = 0
        warnings.warn("Vectors are already aligned (parallel)!", RuntimeWarning)
    return {'axis': rotation_axis, 'angle': angle}

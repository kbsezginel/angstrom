"""
--- Ångström ---
Geometric operations for Ångström Python package.
"""
import numpy as np
import periodictable


def get_molecule_center(atoms, coordinates, mass=True):
    """ Calculate center of mass or geometric center for given coordinates and atom names of a molecule.

    Args:
        - atoms (ndarray): List of element names
        - coordinates (ndarray): List of coordinates (2D list)
        - mass (bool): Use atomic masses (True) or calculate geometric center (False)

    Returns:
        - ndarray: Center coordinate
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

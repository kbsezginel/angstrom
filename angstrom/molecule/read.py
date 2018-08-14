"""
--- Ångström ---
Methods for reading chemical file formats.
"""
import numpy as np


def read_xyz(filename):
    """
    Read xyz file format.

    Parameters
    ----------
    filename : str
        xyz file name.

    Returns
    -------
    dict
        atom names and coordinates:
        -> {'atoms': ['C', ...], 'coordinates': [[x1, y1, z1], ...]}.

    """
    with open(filename, 'r') as xyz_file:
        xyz_lines = xyz_file.readlines()
    n_atoms = int(xyz_lines[0].strip())
    header = xyz_lines[1].strip()
    atoms, coordinates = np.empty((n_atoms,), dtype='U2'), np.empty((n_atoms, 3))
    for i, line in enumerate(xyz_lines[2:]):
        atoms[i] = line.split()[0]
        coordinates[i] = [float(i) for i in line.split()[1:4]]
    return dict(atoms=atoms, coordinates=coordinates, header=header)

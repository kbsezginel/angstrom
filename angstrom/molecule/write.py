"""
Methods for writing chemical file formats.
"""


def write_xyz(fileobj, atoms, coordinates, header='mol'):
    """ Write given atomic coordinates to file object in xyz format

    Args:
        - fileobj (file object): File object for the xyz file
        - atoms (list): List of atom names
        - coordinates (list): List of atomic coordinates

    Returns:
        - None: Creates a new file
    """
    fileobj.write(str(len(coordinates)) + '\n')
    fileobj.write(header + '\n')
    format = '%s %.4f %.4f %.4f\n'
    for atom, coor in zip(atoms, coordinates):
        fileobj.write(format % (atom, coor[0], coor[1], coor[2]))
    fileobj.flush()

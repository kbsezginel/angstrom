"""
--- Ångström ---
Methods for writing chemical file formats.
"""


def write_xyz_traj(fileobj, atoms, coordinates, headers=None):
    """ Write given atomic coordinates to file object in xyz format

    Args:
        - fileobj (file object): File object for the xyz file
        - atoms (list): List of atom names
        - coordinates (list): List of atomic coordinates
        - headers (list): List of strings to write in the second line as header (optional)

    Returns:
        - None: Creates a new file
    """
    n_frames = len(atoms)  # Maybe check if n_frames is same for all???
    if headers is None:
        headers = ['angstrom - %i' % i for i in range(n_frames)]
    xyz_format = '%-2s %7.4f %7.4f %7.4f\n'
    for frame_atoms, frame_coors, frame_header in zip(atoms, coordinates, headers):
        fileobj.write('%i\n' % len(frame_atoms))
        fileobj.write('%s\n' % frame_header)
        for atom, coor in zip(frame_atoms, frame_coors):
            fileobj.write(xyz_format % (atom, coor[0], coor[1], coor[2]))
        fileobj.flush()

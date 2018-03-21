"""
--- Ångström ---
Methods for writing chemical file formats.
"""


def write_xyz(fileobj, atoms, coordinates, header='angstrom'):
    """ Write given atomic coordinates to file object in xyz format

    Args:
        - fileobj (file object): File object for the xyz file
        - atoms (list): List of atom names
        - coordinates (list): List of atomic coordinates
        - header (str): File header

    Returns:
        - None: Creates a new file
    """
    fileobj.write(str(len(coordinates)) + '\n')
    fileobj.write(header + '\n')
    xyz_format = '%-2s %7.4f %7.4f %7.4f\n'
    for atom, coor in zip(atoms, coordinates):
        fileobj.write(xyz_format % (atom, coor[0], coor[1], coor[2]))
    fileobj.flush()


def write_pdb(fileobj, atoms, coordinates, group=None, header='angstrom'):
    """ Write given atomic coordinates to file object in pdb format

    Args:
        - fileobj (file object): File object for the pdb file
        - atoms (list): List of atom names
        - coordinates (list): List of atomic coordinates
        - group (list or None): Residue number for each atom
        - header (str): File header

    Returns:
        - None: Creates a new file
    """
    fileobj.write('HEADER    %s\n' % header)
    pdb_format = 'HETATM%5d%3s  M%4i %3i     %8.3f%8.3f%8.3f  1.00  0.00          %2s\n'
    if group is None:
        group = [1] * len(atoms)
    for atom_index, (atom_name, atom_coor) in enumerate(zip(atoms, coordinates), start=1):
        x, y, z = atom_coor
        residue_no = group[atom_index - 1]
        fileobj.write(pdb_format % (atom_index, atom_name, residue_no, residue_no, x, y, z, atom_name.rjust(2)))
    fileobj.write('END\n')
    fileobj.flush()

"""
--- Ångström ---
Methods for writing chemical file formats.
"""
import os


def write_molecule(filename, atoms, coordinates, bonds=None, group=None, header='angstrom'):
    """ Write molecule file.

    Args:
        - filename (str): Molecule file name, file format extracted from file extension (formats: xyz | pdb)
        - atoms (list): List of atom names
        - coordinates (list): List of atomic coordinates
        - bonds (list): Atomic bonding (used in pdb format)
        - header (str): Molecule file header
        - group (list): Atom grouping (used in pdb format)

    Returns:
        - Writes molecule information to given file name.
    """
    file_format = os.path.splitext(filename)[1].replace('.', '')
    with open(filename, 'w') as fileobj:
        if file_format == 'xyz':
            write_xyz(fileobj, atoms, coordinates, header)
        elif file_format == 'pdb':
            write_pdb(fileobj, atoms, coordinates, bonds=bonds, group=group, header=header)


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


def write_pdb(fileobj, atoms, coordinates, bonds=None, group=None, header='angstrom'):
    """ Write given atomic coordinates to file object in pdb format

    Args:
        - fileobj (file object): File object for the pdb file
        - atoms (list): List of atom names
        - coordinates (list): List of atomic coordinates
        - bonds (list): Atom bonding
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
    if bonds is not None:
        # write bonds
        pass
    fileobj.write('END\n')
    fileobj.flush()

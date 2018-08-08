"""
--- Ångström ---
Methods for writing chemical file formats.
"""
import os
from .cell import Cell


def write_molecule(filename, atoms, coordinates, bonds=None, group=None, cell=None, header='angstrom'):
    """
    Write molecule file. Supprted formats -> (xyz | pdb | cif)
    The file format is extracted from the file extension.

    Parameters
    ----------
    filename : str
        Molecule file name.
    atoms : list
        List of atom names.
    coordinates : list
        List of atomic coordinates.
    bonds : list
        Atomic bonding (used in pdb format).
    group : list
        Atom grouping (used in pdb format).
    cell : list
        Unit cell parameters -> [a, b, c, alpha, beta, gamma] (used in cif format).
    header : str
        Molecule file header.

    Returns
    -------
    None
        Writes molecule information to given file name.

    """
    file_format = os.path.splitext(filename)[1].replace('.', '')
    with open(filename, 'w') as fileobj:
        if file_format == 'xyz':
            write_xyz(fileobj, atoms, coordinates, header=header)
        elif file_format == 'pdb':
            write_pdb(fileobj, atoms, coordinates, bonds=bonds, group=group, header=header)
        elif file_format == 'cif':
            write_cif(fileobj, atoms, coordinates, cell=cell, header=header)


def write_xyz(fileobj, atoms, coordinates, header='angstrom'):
    """
    Write given atomic coordinates to file object in xyz format.

    Parameters
    ----------
    fileobj : file object
        File object for the xyz file.
    atoms : list
        List of atom names.
    coordinates : list
        List of atomic coordinates.
    header : str
        File header.

    Returns
    -------
    None
        Creates a new .xyz file.

    """
    fileobj.write(str(len(coordinates)) + '\n')
    fileobj.write(header + '\n')
    xyz_format = '%-2s %7.4f %7.4f %7.4f\n'
    for atom, coor in zip(atoms, coordinates):
        fileobj.write(xyz_format % (atom, coor[0], coor[1], coor[2]))
    fileobj.flush()


def write_pdb(fileobj, atoms, coordinates, bonds=None, group=None, header='angstrom'):
    """
    Write given atomic coordinates to file object in pdb format.

    Parameters
    ----------
    fileobj : file object
        File object for the pdb file.
    atoms : list
        List of atom names.
    coordinates : list
        List of atomic coordinates.
    bonds : list
        Atom bonding.
    group : list or None
        Residue number for each atom.
    header : str
        File header.

    Returns
    -------
    None
        Creates a new .pdb file.

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
        for atom in range(1, len(atoms) + 1):
            atom_bonds = [atom]
            for b in bonds:
                if atom == b[0] + 1:
                    atom_bonds.append(b[1] + 1)
                elif atom == b[1] + 1:
                    atom_bonds.append(b[0] + 1)
            fileobj.write('CONECT' + ' %4i' * len(atom_bonds) % tuple(atom_bonds) + '\n')
    fileobj.write('END\n')
    fileobj.flush()


def write_cif(fileobj, atoms, coordinates, cell=None, header='angstrom'):
    """
    Write given atomic coordinates to file in cif format.

    Parameters
    ----------
    fileobj : file object
        File object for the xyz file.
    atoms : list
        List of atom names.
    coordinates : list
        List of atomic coordinates.
    cell : list
        Unit cell parameters -> [a, b, c, alpha, beta, gamma].
    header : str
        File header.

    Returns
    -------
    None
        Creates a new .cif file.

    """
    if cell is None:
        cell = [1, 1, 1, 90, 90, 90]
    else:
        uc = Cell(cell)
        coordinates = [uc.car2frac(c) for c in coordinates]
    fileobj.write('data_%s\n' % header)
    fileobj.write("_symmetry_space_group_name_H-M    'P1'\n")
    fileobj.write('_symmetry_Int_Tables_number       1\n')
    fileobj.write('_symmetry_cell_setting            triclinic\n')
    fileobj.write('_cell_length_a                   %7.4f\n' % cell[0])
    fileobj.write('_cell_length_b                   %7.4f\n' % cell[1])
    fileobj.write('_cell_length_c                   %7.4f\n' % cell[2])
    fileobj.write('_cell_angle_alpha                %7.4f\n' % cell[3])
    fileobj.write('_cell_angle_beta                 %7.4f\n' % cell[4])
    fileobj.write('_cell_angle_gamma                %7.4f\n' % cell[5])
    fileobj.write('loop_\n')
    fileobj.write('_atom_site_label\n')
    fileobj.write('_atom_site_type_symbol\n')
    fileobj.write('_atom_site_fract_x\n')
    fileobj.write('_atom_site_fract_y\n')
    fileobj.write('_atom_site_fract_z\n')
    cif_format = '%s%-4i %2s %7.4f %7.4f %7.4f\n'
    for i, (atom, coor) in enumerate(zip(atoms, coordinates)):
        fileobj.write(cif_format % (atom, i, atom, coor[0], coor[1], coor[2]))
    fileobj.flush()

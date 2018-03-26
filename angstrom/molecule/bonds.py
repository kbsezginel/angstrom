"""
--- Ångström ---
Molecular bonding estimation for Ångström Python package.
"""
# Molecular Single-Bond Covalent Radii for Elements 1-118 by Pyykko et al. doi: 10.1002/chem.200800987
rcov = {'H': 0.32, 'He': 0.46, 'Li': 1.33, 'Be': 1.02, 'B': 0.85, 'C': 0.75, 'N': 0.71,
        'O': 0.63, 'F': 0.64, 'Ne': 0.67, 'Na': 1.55, 'Mg': 1.39, 'Al': 1.26, 'Si': 1.16,
        'P': 1.11, 'S': 1.03, 'Cl': 0.99, 'Ar': 0.96, 'K': 1.96, 'Ca': 1.71, 'Sc': 1.48,
        'Ti': 1.36, 'V': 1.34, 'Cr': 1.22, 'Mn': 1.19, 'Fe': 1.16, 'Co': 1.11, 'Ni': 1.10,
        'Cu': 1.12, 'Zn': 1.18, 'Ga': 1.24, 'Ge': 1.21, 'As': 1.21, 'Se': 1.16, 'Br': 1.14,
        'Kr': 1.17, 'Rb': 2.10, 'Sr': 1.85, 'Y': 1.63, 'Zr': 1.54, 'Nb': 1.47, 'Mo': 1.38,
        'Tc': 1.28, 'Ru': 1.25, 'Rh': 1.25, 'Pd': 1.20, 'Ag': 1.28, 'Cd': 1.36, 'In': 1.42,
        'Sn': 1.40, 'Sb': 1.40, 'Te': 1.36, 'I': 1.33, 'Xe': 1.31, 'Cs': 2.32, 'Ba': 1.96,
        'Hf': 1.52, 'Ta': 1.46, 'W': 1.37, 'Re': 1.31, 'Os': 1.29, 'Ir': 1.22, 'Pt': 1.23,
        'Au': 1.24, 'Hg': 1.33, 'Tl': 1.44, 'Pb': 1.44, 'Bi': 1.51, 'Po': 1.45, 'At': 1.47,
        'Ru': 1.42, 'Fr': 2.23, 'Ra': 2.01, 'Rf': 1.57, 'Db': 1.49, 'Sg': 1.43, 'Bh': 1.41,
        'Hs': 1.34, 'Mt': 1.29, 'Ds': 1.28, 'Rg': 1.21, 'La': 1.80, 'Ce': 1.63, 'Pr': 1.76,
        'Nd': 1.74, 'Pm': 1.73, 'Sm': 1.72, 'Eu': 1.68, 'Gd': 1.69, 'Tb': 1.68, 'Dy': 1.67,
        'Ho': 1.66, 'Er': 1.65, 'Tm': 1.64, 'Yb': 1.70, 'Lu': 1.62, 'Ac': 1.86, 'Th': 1.75,
        'Pa': 1.69, 'U': 1.70, 'Np': 1.17, 'Pu': 1.72, 'Am': 1.66, 'Cm': 1.66, 'Bk': 1.68,
        'Cf': 1.68, 'Es': 1.65, 'Fm': 1.67, 'Md': 1.73, 'No': 1.76, 'Lr': 1.61}


def get_bonds(atoms, coordinates, RADIUS_BUFFER=0.45, MIN_BOND_DISTANCE=0.16):
    """Estimate molecular bonding.

    Args:
        - atoms (list): List of atom names
        - coordinates (list): List of atomic coordinates
        - RADIUS_BUFFER (float): Atomic radius buffer (Å)
        - MIN_BOND_DISTANCE (float): Minimum bonding distance (Å)

    Returns:
         list: List of bonded atoms
    """
    coors_z = list(enumerate(coordinates))
    coors_z = sorted(coors_z, key=lambda x: x[1][2])
    # Find the maximum radius among all atoms
    max_rad = max([rcov[i] for i in set(atoms)])
    bonds = []
    for i in range(0, len(coors_z)):
        max_cutoff = rcov[atoms[coors_z[i][0]]] + max_rad + RADIUS_BUFFER
        for j in range(i + 1, len(coors_z)):
            if abs(coors_z[j][1][2] - coors_z[i][1][2]) > max_cutoff:
                break
            distance = ((coors_z[j][1][0] - coors_z[i][1][0]) ** 2 +
                        (coors_z[j][1][1] - coors_z[i][1][1]) ** 2 +
                        (coors_z[j][1][2] - coors_z[i][1][2]) ** 2) ** 0.5
            max_bond_distance = (rcov[atoms[coors_z[i][0]]] + rcov[atoms[coors_z[j][0]]] + RADIUS_BUFFER)
            if distance >= MIN_BOND_DISTANCE and distance <= max_bond_distance:
                bonds.append(tuple(sorted((coors_z[i][0], coors_z[j][0]))))
    return bonds

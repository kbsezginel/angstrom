"""
--- Ångström ---
Molecular improper determination and calculation for Ångström Python package.
"""
from itertools import combinations


def get_impropers(bonds):
    """
    Iterate over bonds to get impropers.
    Choose all three bonds that have one atom in common.
    For each set of bonds you have 3 impropers where one of the noncommon atoms is out of plane.

    Parameters
    ----------
    bonds : list
        List of atom ids that make up bonds.

    Returns
    -------
    list
        List of atom id quadruplets that make up a improper.
    """
    impropers, checked = [], []
    for bond in bonds:
        for atom in bond:
            if atom not in checked:
                bonded_list = []
                for bond2 in bonds:
                    if atom in bond2:
                        bonded_list.append(bond2[1 - bond2.index(atom)])
                if len(bonded_list) >= 3:
                    for triplet in combinations(bonded_list, 3):
                        for out_of_plane in triplet:
                            imp = tuple([out_of_plane, atom] + sorted([i for i in triplet if i != out_of_plane]))
                            impropers.append(imp)
            checked.append(atom)
    return sorted(impropers)

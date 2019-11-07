"""
--- Ångström ---
Tests get chemical formula function for molecules.
"""
import os
from angstrom import Molecule


test_dir = os.path.abspath(os.path.dirname(__file__))
benzene_xyz = os.path.join(test_dir, 'benzene.xyz')
piyzaz111_xyz = os.path.join(test_dir, 'PIYZAZ_111.xyz')
piyzaz222_xyz = os.path.join(test_dir, 'PIYZAZ_222.xyz')


def test_benzene_chemical_formula():
    """ Tests chemical formula for benzene molecule """
    benzene = Molecule(read=benzene_xyz)
    assert benzene.get_chemical_formula() == {'C': 6, 'H': 6}


def test_piyzaz_chemical_formula():
    """ Testing chemical formula for PIYZAZ in 111 and 222 packing"""
    piyzaz111 = Molecule(read=piyzaz111_xyz)
    assert piyzaz111.get_chemical_formula() == {'C': 8, 'Cd': 2}
    piyzaz222 = Molecule(read=piyzaz222_xyz)
    assert piyzaz222.get_chemical_formula() == {'C': 64, 'Cd': 16}

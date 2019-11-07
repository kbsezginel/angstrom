"""
--- Ångström ---
Tests aligning molecules.
"""
import os
from angstrom import Molecule


benzene_xyz = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'benzene.xyz')
piyzaz111_xyz = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'PIYZAZ_111.xyz')
piyzaz222_xyz = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'PIYZAZ_222.xyz')


def test_benzene_chemical_formula():
    """ Tests chemical formula for benzene molecule """
    benzene = Molecule(read=benzene_xyz)
    assert benzene.get_chemical_formula() == {'C': 6, 'H': 6}


def test_piyzaz_chemical_formula():
    """ Testing chemical formula for PIYZAZ """
    piyzaz111 = Molecule(read=piyzaz111_xyz)
    assert piyzaz111.get_chemical_formula() == {'C': 8, 'Cd': 2}
    piyzaz222 = Molecule(read=piyzaz222_xyz)
    assert piyzaz222.get_chemical_formula() == {'C': 64, 'Cd': 16}

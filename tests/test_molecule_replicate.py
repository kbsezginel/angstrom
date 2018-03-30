"""
--- Ångström ---
Tests building a supercell by replicating the cell for a molecule object.
"""
from angstrom import Molecule
import numpy as np
import os


piyzaz111_xyz = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'PIYZAZ_111.xyz')
piyzaz222_xyz = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'PIYZAZ_222.xyz')
piyzaz231_xyz = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'PIYZAZ_231.xyz')
piyzaz444_xyz = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'PIYZAZ_444.xyz')
piyzaz_cell_parameters = [8.9950, 8.9950, 8.9950, 60, 60, 60]


def test_piyzaz_replication_2_2_2_without_centering():
    """Tests replicating PIYZAZ (CCDC) 2x2x2 without centering.
    Reference structure is generated using Mercury software."""
    piyzaz = Molecule(read=piyzaz111_xyz)
    piyzaz.set_cell(piyzaz_cell_parameters)
    piyzaz222 = piyzaz.replicate([2, 2, 2], center=False)

    piyzaz222_ref = Molecule(read=piyzaz222_xyz)
    assert np.allclose(piyzaz222.coordinates, piyzaz222_ref.coordinates)
    assert set(piyzaz222.atoms) == set(piyzaz222_ref.atoms)
    assert piyzaz222.cell.a == piyzaz.cell.a * 2
    assert piyzaz222.cell.b == piyzaz.cell.b * 2
    assert piyzaz222.cell.c == piyzaz.cell.c * 2
    assert piyzaz222.cell.alpha == piyzaz.cell.alpha
    assert piyzaz222.cell.beta == piyzaz.cell.beta
    assert piyzaz222.cell.gamma == piyzaz.cell.gamma


def test_piyzaz_replication_2_3_1_without_centering():
    """Tests replicating PIYZAZ (CCDC) 2x3x1 without centering.
    Reference structure is generated using Mercury software."""
    piyzaz = Molecule(read=piyzaz111_xyz)
    piyzaz.set_cell(piyzaz_cell_parameters)
    piyzaz231 = piyzaz.replicate([2, 3, 1], center=False)

    piyzaz231_ref = Molecule(read=piyzaz231_xyz)
    assert np.allclose(piyzaz231.coordinates, piyzaz231_ref.coordinates)
    assert set(piyzaz231.atoms) == set(piyzaz231_ref.atoms)
    assert piyzaz231.cell.a == piyzaz.cell.a * 2
    assert piyzaz231.cell.b == piyzaz.cell.b * 3
    assert piyzaz231.cell.c == piyzaz.cell.c * 1
    assert piyzaz231.cell.alpha == piyzaz.cell.alpha
    assert piyzaz231.cell.beta == piyzaz.cell.beta
    assert piyzaz231.cell.gamma == piyzaz.cell.gamma


def test_piyzaz_replication_2_2_2_with_centering():
    """Tests replicating PIYZAZ (CCDC) 2x2x2 with centering.
    Reference structure is generated using Mercury software."""
    piyzaz = Molecule(read=piyzaz111_xyz)
    piyzaz.set_cell(piyzaz_cell_parameters)
    piyzaz222 = piyzaz.replicate([2, 2, 2], center=True)

    # Move the reference structure so that it's centered to original cell position
    piyzaz222_ref = Molecule(read=piyzaz222_xyz)
    transvec = np.sum(piyzaz.cell.vectors, axis=0) * -1 / 2
    piyzaz222_ref.translate(transvec)
    assert np.allclose(piyzaz222.coordinates, piyzaz222_ref.coordinates)
    assert set(piyzaz222.atoms) == set(piyzaz222_ref.atoms)
    assert piyzaz222.cell.a == piyzaz.cell.a * 2
    assert piyzaz222.cell.b == piyzaz.cell.b * 2
    assert piyzaz222.cell.c == piyzaz.cell.c * 2
    assert piyzaz222.cell.alpha == piyzaz.cell.alpha
    assert piyzaz222.cell.beta == piyzaz.cell.beta
    assert piyzaz222.cell.gamma == piyzaz.cell.gamma


def test_piyzaz_replication_4_4_4_without_centering():
    """Tests replicating PIYZAZ (CCDC) 4x4x4 without centering.
    Reference structure is generated using Mercury software."""
    piyzaz = Molecule(read=piyzaz111_xyz)
    piyzaz.set_cell(piyzaz_cell_parameters)
    piyzaz444 = piyzaz.replicate([4, 4, 4], center=False)

    piyzaz444_ref = Molecule(read=piyzaz444_xyz)
    assert np.allclose(piyzaz444.coordinates, piyzaz444_ref.coordinates)
    assert set(piyzaz444.atoms) == set(piyzaz444_ref.atoms)
    assert piyzaz444.cell.a == piyzaz.cell.a * 4
    assert piyzaz444.cell.b == piyzaz.cell.b * 4
    assert piyzaz444.cell.c == piyzaz.cell.c * 4
    assert piyzaz444.cell.alpha == piyzaz.cell.alpha
    assert piyzaz444.cell.beta == piyzaz.cell.beta
    assert piyzaz444.cell.gamma == piyzaz.cell.gamma

"""
--- Ångström ---
Tests cell vectors calculation.
"""
from angstrom.molecule import Cell
import numpy as np


def test_cubic_unit_cell_should_return_cubic_vectors():
    # Parameters for ECOLEP_clean from CoRE database and expected results from Avogadro
    expected_vectors = [[18.64000, 0.00000, 0.00000],
                        [0.00000, 18.64000, 0.00000],
                        [0.00000, 0.00000, 18.64000]]
    cell = Cell([18.64000, 18.64000, 18.64000, 90.0, 90.0, 90.0])
    cell.calculate_vectors()
    assert np.allclose(cell.vectors, expected_vectors)


def test_orthorhombic_unit_cell_should_return_orthorhombic_vectors():
    # Parameters for MOGYAI_clean from CoRE database and expected results from Avogadro
    expected_vectors = [[10.55690, 0.00000, 0.00000],
                        [0.00000, 14.84590, 0.00000],
                        [0.00000, 0.00000, 19.06630]]
    cell = Cell([10.55690, 14.84590, 19.06630, 90.0, 90.0, 90.0])
    cell.calculate_vectors()
    assert np.allclose(cell.vectors, expected_vectors)


def test_trigonal_unit_cell_should_return_trigonal_vectors():
    # Parameters for MIHHER_clean from CoRE database and expected results from Avogadro
    expected_vectors = [[32.15390, 0.00000, 0.00000],
                        [16.07695, 27.84609, 0.00000],
                        [16.07695, 9.28203, 26.25355]]
    cell = Cell([32.15390, 32.15390, 32.15390, 60.0, 60.0, 60.0])
    cell.calculate_vectors()
    assert np.allclose(cell.vectors, expected_vectors)


def test_tetragonal_unit_cell_should_return_tetragonal_vectors():
    # Parameters for LAVTOT_clean from CoRE database and expected results from Avogadro
    expected_vectors = [[10.26700, 0.00000, 0.00000],
                        [0.00000, 10.26700, 0.00000],
                        [0.00000, 0.00000, 14.46200]]
    cell = Cell([10.26700, 10.26700, 14.46200, 90.0, 90.0, 90.0])
    cell.calculate_vectors()
    assert np.allclose(cell.vectors, expected_vectors)


def test_hexagonal_unit_cell_should_return_hexagonal_vectors():
    # Parameters for cm301726k_si_004_clean from CoRE database and expected results from Avogadro
    expected_vectors = [[12.57380, 0.00000, 0.00000],
                        [-6.2869, 10.88923, 0.00000],
                        [0.00000, 0.00000, 14.33400]]
    cell = Cell([12.57380, 12.57380, 14.33400, 90.00000, 90.00000, 120.00000])
    cell.calculate_vectors()
    assert np.allclose(cell.vectors, expected_vectors)


def test_monoclinic_unit_cell_should_return_monoclinic_vectors():
    # Parameters for OJAKOA_clean from CoRE database and expected results from Avogadro
    expected_vectors = [[9.01670, 0.00000, 0.00000],
                        [-3.61984, 14.69194, 0.00000],
                        [0.00000, 0.00000, 16.82840]]
    cell = Cell([9.01670, 15.13130, 16.82840, 90.00000, 90.00000, 103.84100])
    cell.calculate_vectors()
    assert np.allclose(cell.vectors, expected_vectors)


def test_triclinic_unit_cell_should_return_triclinic_vectors():
    # Parameters for UVARIT_clean from CoRE database and expected results from Avogadro
    expected_vectors = [[8.40900, 0.00000, 0.00000],
                        [2.09071, 13.32498, 0.00000],
                        [1.04535, 6.66249, 12.41697]]
    cell = Cell([8.40900, 13.48800, 14.13020, 61.49240, 85.75740, 81.08290])
    cell.calculate_vectors()
    assert np.allclose(cell.vectors, expected_vectors)

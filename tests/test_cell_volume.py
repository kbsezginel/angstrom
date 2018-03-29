"""
--- Ångström ---
Tests cell volume calculation.
"""
from angstrom.molecule import Cell
import numpy as np


def test_cubic_unit_cell_should_return_correct_cell_volume():
    # Parameters for ECOLEP_clean from CoRE database and expected results from Avogadro
    expected_volume = 6476.46
    cell = Cell([18.64000, 18.64000, 18.64000, 90.0, 90.0, 90.0])
    cell.calculate_volume()
    assert np.isclose(cell.volume, expected_volume)


def test_orthorhombic_unit_cell_should_return_correct_cell_volume():
    # Parameters for MOGYAI_clean from CoRE database and expected results from Avogadro
    expected_volume = 2988.2
    cell = Cell([10.55690, 14.84590, 19.06630, 90.0, 90.0, 90.0])
    cell.calculate_volume()
    assert np.isclose(cell.volume, expected_volume)


def test_trigonal_unit_cell_should_return_correct_cell_volume():
    # Parameters for MIHHER_clean from CoRE database and expected results from Avogadro
    expected_volume = 23506.4
    cell = Cell([32.15390, 32.15390, 32.15390, 60.0, 60.0, 60.0])
    cell.calculate_volume()
    assert np.isclose(cell.volume, expected_volume)


def test_tetragonal_unit_cell_should_return_correct_cell_volume():
    # Parameters for LAVTOT_clean from CoRE database and expected results from Avogadro
    expected_volume = 1524.46
    cell = Cell([10.26700, 10.26700, 14.46200, 90.0, 90.0, 90.0])
    cell.calculate_volume()
    assert np.isclose(cell.volume, expected_volume)


def test_hexagonal_unit_cell_should_return_correct_cell_volume():
    # Parameters for cm301726k_si_004_clean from CoRE database and expected results from Avogadro
    expected_volume = 1962.6
    cell = Cell([12.57380, 12.57380, 14.33400, 90.00000, 90.00000, 120.00000])
    cell.calculate_volume()
    assert np.isclose(cell.volume, expected_volume)


def test_monoclinic_unit_cell_should_return_correct_cell_volume():
    # Parameters for OJAKOA_clean from CoRE database and expected results from Avogadro
    expected_volume = 2229.31
    cell = Cell([9.01670, 15.13130, 16.82840, 90.00000, 90.00000, 103.84100])
    cell.calculate_volume()
    assert np.isclose(cell.volume, expected_volume)


def test_triclinic_unit_cell_should_return_correct_cell_volume():
    # Parameters for UVARIT_clean from CoRE database and expected results from Avogadro
    expected_volume = 1391.32
    cell = Cell([8.40900, 13.48800, 14.13020, 61.49240, 85.75740, 81.08290])
    cell.calculate_volume()
    assert np.isclose(cell.volume, expected_volume)

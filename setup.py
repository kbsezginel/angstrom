"""
--- Ångström ---
Ångström Python package setup file.
"""
from setuptools import setup, find_packages


setup(
    name="angstrom",
    version="0.1.0",
    description="Tools for basic molecular operations with minimal-dependency",
    author="Kutay B. Sezginel",
    author_email="kbs37@pitt.edu",
    url='https://github.com/kbsezginel/angstrom',
    include_package_data=True,
    packages=find_packages(),
    install_requires=['pytest',
                      'numpy',
                      'periodictable']
)

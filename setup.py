"""
--- Ångström ---
Ångström Python package setup file.
"""
from setuptools import setup, find_packages


setup(
    name="angstrom",
    version="0.2.0",
    description="Tools for basic molecular operations with minimal-dependency",
    author="Kutay B. Sezginel",
    author_email="kbs37@pitt.edu",
    url='https://github.com/kbsezginel/angstrom',
    include_package_data=True,
    packages=find_packages(),
    install_requires=['numpy',
                      'periodictable',
                      'pyyaml'],
    extras_require={
        'docs': [
            'sphinx',
            'sphinxcontrib-napoleon',
            'sphinx_rtd_theme',
            'numpydoc',
        ],
        'tests': [
            'pytest',
            'pytest-cov',
            'pytest-pep8',
            'tox',
        ],
        'notebook-vis': ['nglview']
    },
    tests_require=[
        'pytest',
        'pytest-cov',
        'pytest-pep8',
        'tox',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'angstrom=angstrom.cli.angstrom:main'
        ]
    }
)

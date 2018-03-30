"""
--- Ångström ---
Cell class for Ångström Python package.
"""
import numpy as np


class Cell:
    """Cell class for unit cell and periodic boundary operations."""
    def __init__(self, cellpar, atoms=None, coordinates=None):
        """Initialize cell for a molecule with cell parameters. Cell angles in degrees. """
        self.a, self.b, self.c = cellpar[:3]
        self.alpha, self.beta, self.gamma = [np.radians(i) for i in cellpar[3:]]
        if atoms is not None and coordinates is not None:
            self.atoms = atoms
            self.coordinates = coordinates

    def calculate_volume(self):
        """ Calculates cell volume. """
        volume = 1 - np.cos(self.alpha)**2 - np.cos(self.beta)**2 - np.cos(self.gamma)**2
        volume += 2 * np.cos(self.alpha) * np.cos(self.beta) * np.cos(self.gamma)
        self.volume = self.a * self.b * self.c * np.sqrt(volume)
        self.frac_volume = volume / (self.a * self.b * self.c)

    def calculate_vectors(self):
        """ Calculates cell vectors. """
        x_v = [self.a, 0, 0]
        y_v = [self.b * np.cos(self.gamma), self.b * np.sin(self.gamma), 0]
        z_v = [0.0] * 3
        z_v[0] = self.c * np.cos(self.beta)
        z_v[1] = (self.c * self.b * np.cos(self.alpha) - y_v[0] * z_v[0]) / y_v[1]
        z_v[2] = np.sqrt(self.c * self.c - z_v[0] * z_v[0] - z_v[1] * z_v[1])
        self.vectors = [x_v, y_v, z_v]

    def calculate_vertices(self):
        """
        Calculate coordinates of unit cell vertices in the following order:
        (0, 0, 0) - (a, 0, 0) - (b, 0, 0) - (c, 0, 0) - (a, b, 0) - (0, b, c) - (a, 0, c) - (a, b, c)
        """
        if not hasattr(self, 'vectors'):
            self.calculate_vectors()
        vertices = []
        vertices.append([0, 0, 0])
        # (a, 0, 0) - (b, 0, 0) - (c, 0, 0)
        for vec in self.vectors:
            vertices.append(vec)
        # (a, b, 0)
        vertices.append([self.vectors[0][0] + self.vectors[1][0], self.vectors[0][1] + self.vectors[1][1],
                        self.vectors[0][2] + self.vectors[1][2]])
        # (0, b, c)
        vertices.append([self.vectors[1][0] + self.vectors[2][0], self.vectors[1][1] + self.vectors[2][1],
                        self.vectors[1][2] + self.vectors[2][2]])
        # (a, 0, c)
        vertices.append([self.vectors[0][0] + self.vectors[2][0], self.vectors[0][1] + self.vectors[2][1],
                        self.vectors[0][2] + self.vectors[2][2]])
        # (a, b, c)
        vertices.append([self.vectors[0][0] + self.vectors[1][0] + self.vectors[2][0],
                        self.vectors[0][1] + self.vectors[1][1] + self.vectors[2][1],
                        self.vectors[0][2] + self.vectors[1][2] + self.vectors[2][2]])
        self.vertices = vertices

    def supercell(self, replication, center=True):
        """ Builds a supercell for given given replication in a, b, and c directions of the cell.

        Args:
            - replication (list): Replication in cell vectors -> [a, b, c]
            - center (bool): Keep the original cell at the center
        Ex:
            The X represents the original cell.
            The position of the original cell can be selected using the center keyword argument:

                center=True        center=False
                -------------      -------------
                |   |   |   |      |   |   |   |
                -------------      -------------
                |   | X |   |      |   |   |   |
                -------------      -------------
                |   |   |   |      | X |   |   |
                -------------      -------------

        Returns:
            - cell: Supercell with replicated coordinates and atoms
        """
        if not hasattr(self, 'vectors'):
            self.calculate_vectors()
        a_v, b_v, c_v = self.vectors

        # Calculate center translation vectors for each cell
        if center:
            center_trans_vec = []
            for dim, factor in enumerate(replication):
                center_translation = (factor - 1) / 2 * a_v[dim] + (factor - 1) / 2 * b_v[dim]
                center_translation += (factor - 1) / 2 * c_v[dim]
                center_trans_vec.append(center_translation)
        else:
            center_trans_vec = [0, 0, 0]

        # Calculate translation vectors for each cell
        translation_vectors = []
        for a_rep in range(replication[0]):
            for b_rep in range(replication[1]):
                for c_rep in range(replication[2]):
                    a_trans = a_v[0] * a_rep + b_v[0] * b_rep + c_v[0] * c_rep - center_trans_vec[0]
                    b_trans = a_v[1] * a_rep + b_v[1] * b_rep + c_v[1] * c_rep - center_trans_vec[1]
                    c_trans = a_v[2] * a_rep + b_v[2] * b_rep + c_v[2] * c_rep - center_trans_vec[2]
                    translation_vectors.append([a_trans, b_trans, c_trans])

        # Create new cell
        supcellpar = [self.a * replication[0], self.b * replication[1], self.c * replication[2]]
        supcellpar += [np.degrees(i) for i in [self.alpha, self.beta, self.gamma]]
        supcell = Cell(supcellpar)
        supcell.atoms = np.empty((0,), dtype='U2')
        supcell.coordinates = np.empty((0, 3))

        # Calculate supercell coordinates
        for trans_vec in translation_vectors:
            supcell.atoms = np.concatenate((supcell.atoms, self.atoms))
            supcell.coordinates = np.concatenate((supcell.coordinates, self.coordinates + trans_vec))
        return supcell

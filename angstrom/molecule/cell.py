"""
--- Ångström ---
Cell class for Ångström Python package.
"""


class Cell:
    """Cell class for unit cell and periodic boundary operations."""
    def __init__(self, cellpar):
        """Initialize cell for a molecule withh cell parameters."""
        self.a, self.b, self.c, self.alpha, self.beta, self.gamma = cellpar

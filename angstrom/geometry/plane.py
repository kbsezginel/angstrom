"""
Mirror object to create prisms and perform reflections
"""
import numpy as np
from .quaternion import Quaternion


planes = {'xy': ([0, 0, 0], [1, 0, 0], [1, 1, 0]),
          'xz': ([0, 0, 0], [1, 0, 0], [1, 0, 1]),
          'yx': ([0, 0, 0], [0, 1, 0], [1, 1, 0]),
          'yz': ([0, 0, 0], [0, 1, 0], [0, 1, 1]),
          'zx': ([0, 0, 0], [0, 0, 1], [1, 0, 1]),
          'zy': ([0, 0, 0], [0, 0, 1], [0, 1, 1])}


class Plane:
    """ Plane object. Initialized by either giving 3 points or a string (ex: 'xy') for main planes."""
    def __init__(self, *args, size=1):
        if len([*args]) == 3:
            p1, p2, p3 = [np.array(i) * size for i in args]
        elif str(*args) in planes.keys():
            p1, p2, p3 = [np.array(i) * size for i in planes[str(*args)]]
        # Source: http://kitchingroup.cheme.cmu.edu/blog/2015/01/18/Equation-of-a-plane-through-three-points/
        # These two vectors are in the plane
        self.v1 = p3 - p1
        self.v2 = p2 - p1
        # the cross product is a vector normal to the plane
        cp = np.cross(self.v1, self.v2)
        self.a, self.b, self.c = cp
        # This evaluates a * x3 + b * y3 + c * z3 which equals d
        self.d = np.dot(cp, p3)
        self.p1, self.p2, self.p3 = p1, p2, p3

    def reflect(self, point):
        """ Get mirror image of a point through the plane of reflection.

        Args:
            - point (list): 3D point

        Returns:
            - ndarray: Mirror image of the point
        """
        s0 = (self.a * point[0] + self.b * point[1] + self.c * point[2] - self.d)
        s0 /= (self.a**2 + self.b**2 + self.c**2)

        x = point[0] - 2 * s0 * self.a
        y = point[1] - 2 * s0 * self.b
        z = point[2] - 2 * s0 * self.c

        return np.array([x, y, z])

    def grid(self, size, space=1):
        """Calculate grid points for the plane for given grid size and spacing.

        Args:
            - size (float): Grid size
            - space (float): Grid point spacing

        Three points P1(x1, y1, z1), P2(x2, y2, z2), P3(x3, y3, z3)
            P2  o.....o.....o P3
                o.....o.....o
            Pn  o.....o.....o
                o.....o.....o
            P1  o.....o.....o
                     Pm

        Returns:
            - ndarray: Grid points
        """
        grid_points = []
        for m in np.arange(0, size + space, space):
            for n in np.arange(0, size + space, space):
                x = (size - n) * self.p1[0] + (n - m) * self.p2[0] + m * self.p3[0]
                y = (size - n) * self.p1[1] + (n - m) * self.p2[1] + m * self.p3[1]
                z = (size - n) * self.p1[2] + (n - m) * self.p2[2] + m * self.p3[2]
                grid_points.append([x, y, z])
        return np.array(grid_points)

    def get_center(self):
        """ Get center point of the plane ."""
        return self.p1 + (self.p3 - self.p1) / 2

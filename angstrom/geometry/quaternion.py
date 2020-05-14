"""
--- Ångström ---
Quaternion operations for Ångström Python package.
"""
import numpy as np


class Quaternion(object):
    """
    Quaternion class for quaternion operations and 3D rotations.

    """
    def __init__(self, param_list):
        """
        Initialize Quaternion with a 4 element list -> [w, x, y, z].

        Parameters
        ----------
        param_list: list
            Quaternion w, x, y, and z values respectively.

        """
        self.w = param_list[0]
        self.x = param_list[1]
        self.y = param_list[2]
        self.z = param_list[3]
        self.x_axis = [[0, 0, 0], [1, 0, 0]]
        self.y_axis = [[0, 0, 0], [0, 1, 0]]
        self.z_axis = [[0, 0, 0], [0, 0, 1]]

    def __repr__(self):
        return "<Quaternion object w:%s x:%s y:%s z:%s>" % (self.w, self.x, self.y, self.z)

    def __str__(self):
        return "x:%s y:%s z:%s" % (self.x, self.y, self.z)

    def xyz(self):
        """
        Returns x, y, z values of the quaternion in list format.

        Returns
        -------
        list
            A list of x, y, and z values respectively.

        """
        return [self.x, self.y, self.z]

    def np(self):
        """
        Returns numpy array if x, y, z values.

        Returns
        -------
        ndarray
            A numpy array of x, y, and z values respectively.

        """
        return np.array([self.x, self.y, self.z])

    def __mul__(self, quat2):
        """
        Multiply quaternion by another.

        Parameters
        ----------
        quat2: Quaternion
            The quaternion to multiply with.

        Returns
        -------
        Quaternion
            The resulting Quaternion object from the multiplication.

        Examples
        --------
        >>> q1 = Quaternion([1, 2, 3, 4])
        >>> q2 = Quaternion([2, 3, 4, 5])
        >>> q1 * q2
        <Quaternion object w:-36 x:6 y:12 z:12>

        """
        q1, q2 = self, quat2
        w3 = q1.w * q2.w - q1.x * q2.x - q1.y * q2.y - q1.z * q2.z
        x3 = q1.x * q2.w + q1.w * q2.x - q1.z * q2.y + q1.y * q2.z
        y3 = q1.y * q2.w + q1.z * q2.x + q1.w * q2.y - q1.x * q2.z
        z3 = q1.z * q2.w - q1.y * q2.x + q1.x * q2.y + q1.w * q2.z
        return Quaternion([w3, x3, y3, z3])

    def __truediv__(self, quat2):
        """
        Divide one quaternion by another. Performs the operation as q1 * inverse q2.

        Parameters
        ----------
        quat2: Quaternion
            The quaternion to divide with.

        Returns
        -------
        Quaternion
            The resulting Quaternion object from the division.

        Examples
        --------
        >>> q1 = Quaternion([1, 2, 3, 4])
        >>> q2 = Quaternion([2, 3, 4, 5])
        >>> q1 / q2
        <Quaternion object w:0.7407 x:0.0370 y:0.0 z:0.0741>

        """
        return self * quat2.inv()

    def inv(self):
        """
        Returns the inverse of the quaternion as a new quaternion.

        Returns
        -------
        Quaternion
            The inverse of the Quaternion object.

        """
        norm = self.w ** 2 + self.x ** 2 + self.y ** 2 + self.z ** 2
        return Quaternion([self.w / norm, -self.x / norm, -self.y / norm, -self.z / norm])

    def rotation(self, rotation_point, rotation_axis, rotation_angle):
        """
        Rotation of a point around an axis defined by two points in 3D space.
        The direction of rotation is counter-clockwise given that axis is defined as p2 - p1.
        Rotation angle needs to be given in radians.

        Parameters
        ----------
        rotation_point: list
            The point to rotate.
        rotation_axis: tuple or str
            Tuple of 3D points defining the axis of rotation.
            If 'x', 'y', or 'z' is given primary axes are used.
        rotation_angle: float
            Rotation angle in radians.

        Returns
        -------
        Quaternion
            Quaternion with rotated point.

        Examples
        --------
        >>> import numpy as np
        >>> Q = Quaternion([0, 1, 1, 1])
        >>> Q = Q.rotation(Q.xyz(), [-2, 4, 6.1], [0.3, 1.2, -0.76], np.pi/6)
        [2.1192250600275795, 2.2773560513200133, 5.890236840657188]

        """
        if rotation_axis in ['x', 'y', 'z']:
            rotation_axis = getattr(self, f"{rotation_axis}_axis")
        axis_point1, axis_point2 = rotation_axis
        i = axis_point2[0] - axis_point1[0]
        j = axis_point2[1] - axis_point1[1]
        k = axis_point2[2] - axis_point1[2]
        length = np.sqrt(i**2 + j**2 + k**2)
        i = i / length
        j = j / length
        k = k / length
        qp_w = 0
        qp_x = rotation_point[0] - axis_point2[0]
        qp_y = rotation_point[1] - axis_point2[1]
        qp_z = rotation_point[2] - axis_point2[2]
        Q_point = Quaternion([qp_w, qp_x, qp_y, qp_z])

        qr_w = np.cos(rotation_angle / 2.0)
        qr_x = np.sin(rotation_angle / 2.0) * i
        qr_y = np.sin(rotation_angle / 2.0) * j
        qr_z = np.sin(rotation_angle / 2.0) * k
        Q_rot = Quaternion([qr_w, qr_x, qr_y, qr_z])

        Quat = (Q_rot * Q_point) * Q_rot.inv()
        Quat.x = Quat.x + axis_point2[0]
        Quat.y = Quat.y + axis_point2[1]
        Quat.z = Quat.z + axis_point2[2]

        return Quat

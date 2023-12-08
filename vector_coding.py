

from math import cos, sin, acos, sqrt, pi
from random import random



class vector(object):
    'vector class'

    @staticmethod
    def random():
        return vector(-1.0 + 2.0*random(), -1.0 + 2.0*random(), -1.0 + 2.0*random())

    def __init__(self, *args):
        if len(args) == 3:
            self._x = float(args[0]) # make sure it's a float; could be numpy.float64
            self._y = float(args[1])
            self._z = float(args[2])
        elif len(args) == 1 and isinstance(args[0], vector): # make a copy of a vector
            other = args[0]
            self._x = other._x
            self._y = other._y
            self._z = other._z
        else:
            raise TypeError('A vector needs 3 components.')
        self.on_change = self.ignore

    def ignore(self):
        pass

    @property
    def value(self):
        return [self._x, self._y, self._z]
    @value.setter
    def value(self,other):  ## ensures a copy; other is a vector
        self._x = other._x
        self._y = other._y
        self._z = other._z

    def __neg__(self):
        return vector(-self._x, -self._y, -self._z)

    def __pos__(self):
        return self

    def __str__(self):
        return '<{:.6g}, {:.6g}, {:.6g}>'.format(self._x, self._y, self._z)

    def __repr__(self):
        return 'vector({:.6g}, {:.6g}, {:.6g})'.format(self._x, self._y, self._z)

    def __add__(self, other):
        if type(other) is vector:
            return vector(self._x + other._x, self._y + other._y, self._z + other._z)
        return NotImplemented

    def __sub__(self, other):
        if type(other) is vector:
            return vector(self._x - other._x, self._y - other._y, self._z - other._z)
        return NotImplemented

    def __truediv__(self, other): # used by Python 3, and by Python 2 in the presence of __future__ division
        if isinstance(other, (float, int)):
            return vector(self._x / other, self._y / other, self._z / other)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return vector(self._x * other, self._y * other, self._z * other)
        return NotImplemented
    
    def __eq__(self,other):
        if type(self) is vector and type(other) is vector:
            return self.equals(other)
        return False

    def __ne__(self,other):
        if type(self) is vector and type(other) is vector:
            return not self.equals(other)
        return True
    
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self,value):
        self._x = value
        self.on_change()

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self,value):
        self._y = value
        self.on_change()

    @property
    def z(self):
        return self._z
    @z.setter
    def z(self,value):
        self._z = value
        self.on_change()

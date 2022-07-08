import math
from functools import total_ordering

@total_ordering
class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector(x={self.x},y={self.y},z={self.z})"

    def __hash__(self):
        return hash((self.x,self.y,self.z,self.__class__))

    def __str__(self):
        return f'x={self.x},y={self.y},z={self.z}'

    def __eq__(self, other):
        if isinstance(other,self.__class__):
            return hash(self) == hash(other)

    def get_magnitude(self):
        x_sqrt = self.x ** 2
        y_sqrt = self.y ** 2
        z_sqrt = self.z ** 2

        return math.sqrt(sum([x_sqrt,y_sqrt,z_sqrt]))

    def __add__(self, other):
        if isinstance(other,Vector):
            new_vector = eval(repr(self))
            new_vector.y += other.y
            new_vector.x += other.x
            new_vector.z += other.z

            return new_vector

    def __radd__(self, other):
        if isinstance(other, Vector):
            new_vector = eval(repr(self))
            new_vector.y += other.y
            new_vector.x += other.x
            new_vector.z += other.z

            return new_vector

    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other,float):
            new_vector = eval(repr(self))
            new_vector.x *= other
            new_vector.y *= other
            new_vector.z *= other

            return new_vector

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_vector = eval(repr(self))
            new_vector.x *= other
            new_vector.y *= other
            new_vector.z *= other

            return new_vector

    def __gt__(self, other):
        return self.get_magnitude() > other.get_magnitude()

    def __getitem__(self, item):
        try:
            return self.__dict__[item.lower()]
        except:
            return NotImplemented

vector = Vector(1,2,3)
vector2 = Vector(1,2,3)



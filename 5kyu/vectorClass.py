# Vector Class
# https://www.codewars.com/kata/532a69ee484b0e27120000b6/train/python
class Vector:
    def __init__(self, x, y = None, z = None):
        if y != None:
            self.x = x
            self.y = y
            self.z = z
            self.magnitude = (x*x + y*y + z*z)**.5
        else:
            self.x = x[0]
            self.y = x[1]
            self.z = x[2]
            self.magnitude = (x[0]*x[0] + x[1]*x[1] + x[2]*x[2])**.5

    def __repr__(self):
        return f"<{self.x}, {self.y}, {self.z}>"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return self + Vector(-other.x, -other.y, -other.z)

    def __eq__(self, other):
        return all((self.x == other.x, self.y == other.y, self.z == other.z))

    def cross(self, other):
        compx = self.y*other.z - self.z*other.y
        compy = self.z*other.x - self.x*other.z
        compz = self.x*other.y - self.y*other.x
        return Vector(compx, compy, compz)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def to_tuple(self):
        return self.x, self.y, self.z


a = Vector(2, 1, 4)
b = Vector([5, 6, 1])

c = a + b
print(c)

c = a - b
print(c)

c = Vector(5, 6, 1)
print(c == b)

c = a.cross(b)
print(c)

print(a.dot(b))

print(a.to_tuple())

print(str(a))

print(a.magnitude)

print(a.x)
print(a.y)
print(a.z)

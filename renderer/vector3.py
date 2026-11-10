import math
class Vector3:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        return Vector3((self.x + other.x),(self.y + other.y),(self.z + other.z))
    def __sub__(self, other):
        return Vector3((self.x - other.x),(self.y - other.y),(self.z - other.z))
    def __mul__(self, scalar):
        return Vector3((self.x * scalar),(self.y * scalar),(self.z * scalar))
    def __truediv__(self, scalar):
        return Vector3((self.x / scalar),(self.y / scalar),(self.z / scalar))
    def length(self):
        return math.sqrt((self.x**2) + (self.y**2) + (self.z**2))
    def normalize(self):
        length = self.length()
        if length == 0: return Vector3(0,0,0)
        return (self / length)
    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
    def cross(self, other):
        return Vector3(((self.y * other.z) - (self.z *other.y)),((self.z *other.x) - (self.x *other.z)),((self.x *other.y) - (self.y * other.x)))
    def rotate_y(self,rad):
        
        x1 = self.x *math.cos(rad) + self.z *math.sin(rad)
        z1 = -self.x *math.sin(rad) + self.z *math.cos(rad)
        y1 = self.y
        return Vector3(x1,y1,z1)
a = Vector3(2, 3, 5)
b = Vector3(1, 0, -2)

c = a + b

v = Vector3(1, 0, 0)
rotated = v.rotate_y(math.radians(90))

print(rotated.x, rotated.y, rotated.z)
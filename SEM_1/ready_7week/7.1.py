class Vector():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x + other, self.y + other, self.z + other)
    def __radd__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x + other, self.y + other, self.z + other)
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x - other, self.y - other, self.z - other)
    def __rsub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(-(self.x - other), -(self.y - other), -(self.z - other))
    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other, self.z * other)
    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other, self.z * other)
    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x / other, self.y / other, self.z / other)

v1 = Vector(1, 2, 3)
print(isinstance(v1, Vector))
print(v1.x - v1.y)
v2 = Vector(2, 3, 4)
v3 = v2+v1
s4 = v2*v1
v5 = (2*v3*2) / 1
print(v3.x,v3.y,v3.z)
print(s4)
print(v5.x,v5.y,v5.z)
n = int(input("Сколько точек?: "))
v0 = Vector(0, 0, 0)
for i in range(n):
    a = list(map(int, input().split()))
    v0 = v0 + Vector(a[0], a[1], a[2])
print((v0 / n).x, (v0 / n).y, (v0 / n).z)


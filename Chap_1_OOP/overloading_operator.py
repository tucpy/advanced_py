class Vector(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return "Vector(%d,%d)" %(self.a,self.b)
    def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b)

vector1 = Vector(1,2)
print(vector1)
vector2 = Vector(3,4)
print(vector2)
vector3 = vector1 + vector2
print(vector3)
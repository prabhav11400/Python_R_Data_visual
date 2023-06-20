class Vector:
    def __init__(self,a,b,c):
        self.i=a
        self.j=b
        self.k=c
    def __add__(self,v):
        return Vector((self.i+v.i) , (self.j+v.j) ,(self.k+v.k))
    def __mul__(self,v):
        return Vector((self.i*v.i),(self.j*v.j),(self.k*v.k))
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
v1=Vector(1,2,3)
v2=Vector(4,5,6)
print(v1+v2)
print(v1*v2)
print(v1)
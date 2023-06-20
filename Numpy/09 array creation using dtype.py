import numpy as np
a=np.array([10,20,30,400,50])
print(a)
print(a.dtype)

b=np.array(['1','2','3','4','5'])
print(b)
print(b.dtype)

c=np.array(['10','20','30','40','50'])
print(c)
print(c.dtype)

d=np.array(['100','200','300','400','500'])
print(d)
print(d.dtype)

e=np.array(['10','20','30','40','50'],dtype="i")
print(e)
print(e.dtype)

f=np.array(['10','20','30','40','50'],dtype="S")
print(f)
print(f.dtype)

g=np.array(['1','2','3','4','5'],dtype="S")
print(g)
print(g.dtype)

h=np.array([10,20,30,40,50],dtype="U")
print(h)
print(h.dtype)

h2=np.array([10,20,30,40,50],dtype="U1")
print(h2)
print(h2.dtype)

h3=np.array([10,20,30,40,50],dtype="U2")
print(h3)
print(h3.dtype)

h4=np.array([10,20,30,40,50],dtype="U3")
print(h4)
print(h4.dtype)

## changing catatype of an array using astype
a=np.array([10,20,0,40])
print(a)
print(a.dtype)

b=a.astype("U")
print(b)
print(b.dtype)

c=a.astype("f")
print(c)
print(c.dtype)

d=a.astype("bool")
print(d)
print(d.dtype)


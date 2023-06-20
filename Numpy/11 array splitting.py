import numpy as np
a=np.arange(10)
print(a)
print(np.split(a,2))
# print(np.split(a,3)) error ValueError: array split does not result in an equal division
print(np.array_split(a,2))
print(np.array_split(a,3))
print(np.array_split(a,4))
print(np.hsplit(a,2))
# print(np.hsplit(a,3)) ye hsplit is same as split, it only can divide in equal division
# print(np.vsplit(a,2)) ValueError: vsplit only works on arrays of 2 or more dimensions
b=np.arange(6).reshape(2,3)
print(b)
c=np.vsplit(b,2)
print(c)
# d=np.vsplit(b,3) eror ValueError: array split does not result in an equal division
# print(d)
e=np.arange(6).reshape(3,2)
print(e)
f=np.vsplit(e,3)
print(f)
# g=np.vsplit(e,2)
# print(g) ValueError: array split does not result in an equal division
h=np.vsplit(e,1)
print(h)
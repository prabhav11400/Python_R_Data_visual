# (1) concatenate()
import numpy as np
a=np.arange(6).reshape(2,3) # by default [0,6)
print(a)
b=np.arange(7,13).reshape(2,3)
print(b)
c=np.concatenate((a,b)) # by default axis=0, i.e. column wise joining without changing the dimension
print(c)
d=np.concatenate((a,b),axis=0)
print(d)
e=np.concatenate((a,b),axis=1)
print(e)

# (2) stack()
f=np.stack((a,b))
print(f)
g=np.stack((a,b),axis=0)
print(g)
h=np.stack((a,b),axis=1)
print(h)

# (3) vstack()
i=np.vstack((a,b))
print(i)

# (4) hstack()
j=np.hstack((a,b))
print(j)

# (5) dstack()
k=np.dstack((a,b))
print(k)
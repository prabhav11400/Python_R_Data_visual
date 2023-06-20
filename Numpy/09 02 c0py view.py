import numpy as np
a=np.array([1,2,3,4,5])
print(a)
c=a.copy()
print(c)
print(a)
c[1]=100
print(c)
print(a)
#Since c is a copy of a,another array. So any change in c will not change in a

v=a.view()
print(v)
a[2]=-2
print(a)
print(v)
v[3]=-3
print(a)
print(v)
# Since v has referrence of a, so changing in either v or a will change in both a and v



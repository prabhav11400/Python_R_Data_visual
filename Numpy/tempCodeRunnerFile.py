import numpy as np
a=np.array([[10,20,30],[40,50,60]])
print(a)
#play with row major
res1=np.asarray(a,dtype="int",order="C") # row major(10,20,30,40,50,60)
for i in np.nditer(res1):
    print(i)
for i in np.nditer(res1):
    print(i,end=" ")
# Play with column major
res2=np.asarray(a,dtype="int",order="F") # F= column major 10,40,20,50,30,60
print(res2)
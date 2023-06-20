# 1D Array
import numpy as np
a=np.array([1,2,3,4,5,6,7,8])
print(a)
print(a[0],end="_")
print(a[4])
print(a[-1],end="-")
print(a[-8])

# 2D Array
b=np.array([[10,20,30],[40,50,60]])
print(b)
print(b[1,2]) #2nd row ka 3rd(i=2) vala element
print(b[0,0])# 1st row and 1st column ka element
print(b[-1,-2]) #-1= last vala biggest box ka, i=-2 vala element(i.e 2nd last element) i.e. 50

#3D Array
c=np.array([[[10,20,30,40],[50,60,70,80]],[[90,100,110,120],[130,140,150,160]]])
print(c)
print(c[0,1,2]) #0th 2D array ke i=1 vale(second) 1D array, ka i=2(3rd element) vala element 
print(c[0,1,-2]) # 0th 2D array ke i=1 vale(second) 1D array, ka i=-2(second last) vala element 
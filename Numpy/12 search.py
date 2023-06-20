import numpy as  np
a= np.arange(10,100,10)
print(a)
print(np.where(a==40))

b= np.array([10,10,20,30,40,50,60,10,10])
print(np.where(b==10))
print(np.where(b%20==0))

print(np.searchsorted(a,45))
print(np.searchsorted(a,[15,25,35]))

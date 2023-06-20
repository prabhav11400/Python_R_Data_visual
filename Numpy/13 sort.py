import numpy as np
a=np.array([50,40,10,20,30])
print(a)
print(np.sort(a))# by default axis=-1
b=np.array([[50,40,30],[20,10,90]])
print(b)
print(np.sort(b))
print(np.sort(b,axis=0)) # this will sort in columns independentally uper se niche in increasing order

# another very interesting sorting technique
d=np.dtype([('name','S9'),('perc','float')]) # name ka dtype String(lenght 9) and percentage ka dtype float hai
stud=np.array([('ram',90.3),('Shyam',89),('kam',65.3)],dtype=d) # dtype=d likhna mt bhulna
print(stud)
print(np.sort(stud,order="perc"))
print(np.sort(stud,order='name'))
print(np.mod(3,2))
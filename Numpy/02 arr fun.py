########################### asarray() ###############################
# s=b"welcome"
# print(type(s)) 
## asarray() demonstration
# import numpy as np
'''a=np.asarray([10,20,30,40,50])
res1=np.asarray(a,dtype="float",order="C")
print(res1)'''
'''
b=np.array([[10,20,30],[40,50,60]])
print(b)
res2=np.asarray(b,dtype="int",order="F") #F=column major
print(res2) #but no difference
# to observe the difference
for i in np.nditer(res2):
    print(i)
res3=np.asarray(res2,dtype="int",order="C")
print(res3)

import numpy as np
s=b"welcomee"
res5=np.frombuffer(s,dtype="S2")
print(res5)'''
import numpy as np
a=np.array([[10,20,30],[40,50,60]])
print(a)
#play with row major
res1=np.asarray(a,dtype="int",order="C") # row major(10,20,30,40,50,60)
for i in np.nditer(res1): 
    print(i) # to get row major order in a column
for i in np.nditer(res1):
    print(i,end=" ") #  to get row major order in a row
# Play with column major
print("\n")
res2=np.asarray(a,dtype="int",order="F") # F= column major 10,40,20,50,30,60
print(res2)
for i in np.nditer(res2): 
    print(i) # to get column major order in a column
for i in np.nditer(res2):
    print(i,end=" ") #  to get column major order in a row


################################### frombuffer() #################################
print("/n")
s=b"Hello welcome tp python "
c=np.frombuffer(s,dtype="S1",count=-1,offset=0)
print(c)
print("\n")
d=c=np.frombuffer(s,dtype="S2",count=-1,offset=0)
print(d)
print("\n")
e=np.frombuffer(s,dtype="S3",count=-1,offset=0)
print(e)
print("\n")
f=np.frombuffer(s,dtype="S1",count=10,offset=0)
print(f)

#################################### fromiter() ######################################
list=[10,20,30,40,50]
d=np.fromiter(list, dtype="float",count=-1)
s="123"
e=np.fromiter(s,dtype="S1",count=-1)
print(e)
f=np.fromiter(s,dtype="float",count=2)
print(f)




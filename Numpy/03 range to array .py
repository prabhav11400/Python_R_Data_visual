import numpy as np
#arange(start, stop[i-1],stepsize,dtype)
a=np.arange(0,10,2,dtype="int") # arange will not include end point at any cost
print(a)
b=np.arange(0,10,2,dtype="float") # arange will not include end point at any cost
print(b)

#linspace(atart, stop(included by default), num(no. of elements),endpoint, retstep, dtype )
c=np.linspace(0,50)
print(c)
d=np.linspace(0,10,5)
print(d)
e=np.linspace(0,10,5,dtype="int")
print(e)
f=np.linspace(0,10,5,endpoint=False,retstep=True)
print(f)

#logspace(base^start,base^stop,num,endpoint,base,dtype)
arra1=np.logspace(0,10,num=4,endpoint=False,base=2)
print(arra1) #(return array of 2^0, 2^2.5, 2^5, 2^7.5)
arra1=np.logspace(0,10,num=4,endpoint=False,base=2, dtype="int")
print(arra1) #(return array of int(2^0), int(2^2.5), int(2^5), int(2^7.5) )


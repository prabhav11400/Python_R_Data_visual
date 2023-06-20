from matplotlib import pyplot as plt
import numpy as np;
import pandas
x1=[1,2,3,4,5,6,7]
y2 = np.linspace(7,20,100)
y1=[9,8,10,12,11,13,14]
x2=0.929*y2-6.219
plt.xlabel("X")
plt.ylabel("Y")
plt.scatter(y1,x1)
plt.plot(y2,x2,  label='x=0.929y-6.219')
plt.grid()
plt.show()


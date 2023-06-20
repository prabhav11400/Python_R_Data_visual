from matplotlib import pyplot as plt
import numpy as np 
x= np.arange(0,10,2)
y=x*10
plt.plot(x,y)
f1={'family':'cambria','color':'red','size':15}
f2={'family':'calibri','color':'g','size':20}
f3={'family':'arial','color':'k','size':30}
plt.title("MULTIPLE OF 10",fontdict=f1)
plt.xlabel("X-Axis",fontdict=f2)
plt.ylabel("X multiply by 10",fontdict=f3)
plt.show()
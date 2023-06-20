import numpy as np
from matplotlib import pyplot as plt
x=np.linspace(0,2,100)
print(x)
y=1/x**12-1/x**6
print(y)
plt.plot(x,y)
plt.yscale("log")
plt.ylim(10.0e-20,10.0e+24)
plt.show()
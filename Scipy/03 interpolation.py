import matplotlib.pyplot as plt
import  numpy as np
from scipy.interpolate import interp1d
x=np.linspace(0,10,10)
print(x)
y=(x**2)*np.sin(x)
print(y)
plt.scatter(x,y)
# plt.show()
y2=interp1d(x,y,kind="linear")
x2=np.linspace(0, 10,1000)
# print(x2)
# plt.scatter(x2,y2(x2))
plt.plot(x2,y2(x2))
print(y2(8))
plt.show()
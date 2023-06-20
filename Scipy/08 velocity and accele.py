from scipy.misc import derivative
import numpy as np
def f(t):
    return t**3+t**2
t=np.linspace(0,5,5000)
print("v(2) is ",derivative(f,2,dx=1e-6,n=1))
print("a(3) is ",derivative(f,3,dx=1e-6,n=2))

from matplotlib import pyplot as plt 
plt.plot(t,f(t)) # it is displacement curve
plt.plot(t,derivative(f,t,dx=1e-6,n=1)) # Velocity at any point curve
plt.plot(t,derivative(f,t,dx=1e-6,n=2)) # acceleration curve
plt.show()


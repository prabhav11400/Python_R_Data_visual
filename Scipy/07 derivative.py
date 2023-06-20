from matplotlib import pyplot as plt
import numpy as np
from scipy.misc import derivative
def f(x):
    return x**2*np.sin(x)*np.exp(-x)  # x^2.sin(x)e^-x
x=np.linspace(0,1,100)
###############YE VALA METHOD PROPER RESULT NHI DEGA
# f1=derivative(f,x,dx=1e-16)
# plt.plot(x,f(x))
# plt.plot(x,f1(x))
# plt.show()

############## use this method to get proper result. bina store karvaye graph banvao #############
plt.plot(x,f(x))
plt.plot(x,derivative(f,x,dx=1e-6))
plt.plot(x,derivative(f,x,dx=1e-6,n=2))
# plt.plot(x,derivative(f,x,dx=1e-6,n=4))
plt.show()
print(derivative(f,12,dx=1e-6,n=2))
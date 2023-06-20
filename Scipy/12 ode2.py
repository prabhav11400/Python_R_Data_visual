## Suppose a second order ode is coupled, by the following two first order ode's
## (1) y1'=y1+y2^2+3x
## (2) y2'=3y1+y2^3-cos(x)
## we need to define S=(y1,y2)
import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt
def dSdx(S,x):
    y1,y2=S
    return [y1+y2**3+3*x,
            3*y1+y2*3-np.cos(x)]
# specifying initial values of y1, y2
y1_0=0
y2_0=0
S_0=(y1_0,y2_0)
x=np.linspace(0,1,100)
sol=odeint(dSdx,S_0,x)  ## most impoertant part
print(sol)
### To get y1 and y2 separately
print(sol.T)
### Aliter to get only y1 or y2
y1=sol.T[0]
y2=sol.T[1]
print(y1)
print(y2)
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()
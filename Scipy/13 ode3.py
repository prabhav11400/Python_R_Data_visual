## theta'' - sin(theta)=0
## the above ode is coupled, by the following two first order ode's
## (1) theta'=sin(theta)
## (2) omega'=omega
## we need to define S=(theta,omega)

import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint
def dSdt(S,t):
    theta,omega=S
    return [omega,np.sin(theta)]
theta0=np.pi/4
omega0=0
S0=(theta0,omega0)
t=np.linspace(0,20,100)
sol=odeint(dSdt,S0,t)
# theta,omega=sol.T
print(sol.T)
print(sol.T[0])
print(sol.T[1])
print(sol)
theta=sol.T[0] # since theta is given as the first variable of Function S
omega=sol.T[1] # since omega is given as the second variable of function S
plt.plot(t,theta)
plt.plot(t,omega)
plt.show()

# let ode hai v'-3v^2+5=0
# hme ode ke solutions graph se hi clear visualise honge
import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt
def dvdt(v,t):
    return 3*v**2-5
v0=0
t=np.linspace(0,1,100)
sol=odeint(dvdt,v0,t)
print(sol)
print(sol.T)
print(sol.T[0])
plt.plot(t,sol.T[0])
plt.show()

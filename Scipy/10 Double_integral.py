import numpy as np
from scipy.integrate import dblquad
f=lambda y,x:np.sin(x+y**2)
lwr_x=lambda x:-x
upr_x=lambda x:x**2
area=dblquad(f,0,1,lwr_x,upr_x)
print(area)

# ek testing... kya dono limits variable hone pr kuch result aayega
integrand=lambda t,u:t*u
lwr_t=lambda t :t**3
upr_t= lambda t:t**5
lwr_u=lambda u: u**1
upr_u=lambda u: u**2
area=dblquad(integrand,lwr_t,upr_t,lwr_u,upr_u)
print(area)
from scipy.integrate import quad
import numpy as np
integrand=lambda x:(x**2)*np.sin(2*x)*np.exp(-x)
integral,integral_error=quad(integrand,0,1)
print(integral,integral_error)
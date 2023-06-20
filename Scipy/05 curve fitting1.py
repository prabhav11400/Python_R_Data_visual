import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
x_data=np.linspace(0,10,10)
y_data=3*(x_data)**2+2 # these are some discrete/same points. We are giving only (x,y) values
def fun(x,a,b): # a and b are two unknown parameters that computer need to find using the given data
    return a*x**2+b
popt,pcov=curve_fit(fun,x_data,y_data,p0=(1,1)) # p0 initial guess jo ki actually 3,2 hai
print(popt)
a,b=popt
t=np.linspace(0,10,100)
y1=fun(t,a,b)
plt.scatter(x_data,y_data) # ye actual(x,y) ko chart pr scatter plot ke form me dal dega
plt.plot(t,y1) # ye jo new function aya hai, use draw karega, at values of t.
plt.show()

# Now desired curve jo ki mila hai ka use krke kisi bhi x pr y(us curve) ki value find karna
def func2(x):
    return 3*x**2+2 # here a and b milne ke bad manually set kr diya, bs ek variable choda, y=f(x) form bn gya
print(func2(20))



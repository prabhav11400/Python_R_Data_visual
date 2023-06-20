import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
t_data=np.array([0.,0.3448,0.6896,1.0344,1.3796,1.7241,2.0689,2.4137,2.7586,3.1034])
y_data=np.array([4.3303,1.6113,-2.1541,-3.9013,-1.6725,2.1688,3.8663,1.8519,-1.8489,-3.9656])
# plt.plot(t_data,y_data,"o--") to guess phi, A and w . y=Acos(w*t+phi) forn me krna hai
# plt.show()
def func(t,A,w,phi): #A,w,phi are parameters in order
    return A*np.cos(w*t+phi)
popt,pcov=curve_fit(func,t_data,y_data,p0=(4,np.pi,0))
print(popt) # A,w ,phi dega respectivelly

A,w,phi=popt
t=np.linspace(0,10,100)
y=func(t,A,w,phi) # new function jo curve fitting se mila, use y me store kr liya
plt.scatter(t_data,y_data)
plt.plot(t,y)
plt.show()

# known points ke atirikt kisi point pr value pane hetu
def func2(x):
    return A*np.cos(w*x+phi)
print(func2(22))

# to know the variance of parameters A, w , Phi respectively
print(pcov) # it is covariance matrix, jiske main diagonal values, tino parameters ke variances ko darshatre hain
print(np.diag(pcov)) # Variance of parameters respectively

# to get actual error or standard deviations of parameters
print(np.sqrt(np.diag(pcov)))



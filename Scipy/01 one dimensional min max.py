####### Finding Global Minimas ##############

def f(x):
    return (x-3)**2

from scipy.optimize import minimize
res=minimize(f,21)
print(res)

# def f(x):
#     return (x+3)**2+5
# from scipy.optimize import minimize
# res=minimize(f,0)
# print(res)

###### Finding Global Maximas #######

# def f(x,sign=-1.0):
#     return sign*(-x**2+4*x+2)
# from scipy.optimize import minimize
# res=minimize(f,0)
# print(res)

####### Finding local minima and minimum values #######
# def f(x):
#     return (-x**2+4*x+2)
# bnds=[(0,100)]
# from scipy.optimize import minimize
# res=minimize(f,0,bounds=bnds)
# print(res)

####### Finding Local Maxima and maximums ##########
# def f(x,sign=-1):
#     return sign*(-x**2+4*x+2)
# bnds=[(0,2)]
# from scipy.optimize import minimize
# res=minimize(f,0,bounds=bnds)
# print(res)
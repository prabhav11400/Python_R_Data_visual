# # from scipy.optimize import minimize
# # f= lambda x: ((x[0]-1)**2+(x[1]-2.5)**2) # this is circle (x-1)^2+(y-2.5)^2=0

# # cons=({'type':'ineq','fun':lambda x: x[0]-2*x[1]+2}, #constraint x-2y+2>=0 or -(x-2y+2<=0)
# # {'type':'ineq','fun':lambda x: x[0]-2*x[1]+2},# constraint x+2y-6<=0  less than or equal to ko hamesha greater than or equal to me badal kr hi use karo
# # {'type':'ineq','fun':lambda x: -x[0]+2*x[1]+2}) # constraint -x+2y+2>=0

# # bnds=((0,None),(0,None)) # i.e. (0,infinity) both x and y
# # res=minimize(f,(2,0),bounds=bnds,constraints=cons)
# # print(res)

from scipy.optimize import minimize
f= lambda x:((x[0])**3+(x[1])**3+(x[0])**2+4*(x[1])**2+6) # this is circle (x-1)^2+(y-2.5)^2=0

# cons=({'type':'ineq','fun':lambda x: x[0]-2*x[1]+2}, #constraint x-2y+2>=0 or -(x-2y+2<=0)
# {'type':'ineq','fun':lambda x: -x[0]-2*x[1]+6},# constraint x+2y-6<=0  less than or equal to ko hamesha greater than or equal to me badal kr hi use karo
# {'type':'ineq','fun':lambda x: -x[0]+2*x[1]+2}) # constraint -x+2y+2>=0

# bnds=((0,None),(0,None)) # i.e. (0,infinity) both x and y
# bnds=((-2,0),(-3,0))
res=minimize(f,(0,1),method = 'Nelder-Mead')
print(res)

# # Finding Local Maxima

# import numpy as np
# from scipy.optimize import minimize
# def func(x,sign=-1):
#     x1=x[0]
#     x2=x[1]
#     return sign*((x1)**3+(x2)**3+(x1)**2+4*(x2)**2+6)
# result=minimize(func,(-1,-2),method = 'Nelder-Mead')
# print(result)
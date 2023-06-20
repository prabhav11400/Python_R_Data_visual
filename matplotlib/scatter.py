from matplotlib import pyplot as plt
import numpy as np
import random
# x=[1,2,3,4,5,6,7,8,9,10]
# y=[10,20,30,40,50,60,70,80,90,100]
# random.shuffle(y)
# print(x,y)
# plt.grid()
# plt.scatter(x,y)
# plt.show()

x=[1,2,3,4,5,6,7,8,9,10]
y=[10,20,30,40,50,60,70,80,90,100]
y1=[10,20,30,40,50,60,70,80,90,100]
random.shuffle(y)
random.shuffle(y1)
print(x,y)
print(x,y1)
plt.grid()
plt.scatter(x,y,color="purple",marker="*",s=50,linewidth=10,alpha=0.5)
plt.scatter(x,y1,color="red",marker="s",s=30,linewidth=20,alpha=0.75)
plt.show()



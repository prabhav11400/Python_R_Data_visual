from matplotlib import pyplot as plt
x=[1,2,3,4,5]
y1=[2,4,6,8,10]
y2=[3,6,9,12,15]
fig,ax=plt.subplots()
ax2=ax.twinx()
ax.plot(x,y1)
ax2.plot(x,y2)
plt.show()
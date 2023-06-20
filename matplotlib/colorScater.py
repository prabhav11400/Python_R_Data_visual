from matplotlib import pyplot as plt
x=[10,20,30,40,50]
y=[200,300,100,140,500]
colors=[0,30,50,70,200]
sizes=[200,300,100,40,140]

plt.scatter(x,y,c=colors,s=sizes,cmap="Accent",alpha=0.5)
plt.colorbar()
plt.show()
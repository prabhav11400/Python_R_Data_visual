from matplotlib import pyplot as plt
marks=[90,50,40,60,55,44,30,34,10,84]
grade_intervals=[0,40,70,100]

plt.hist(marks,grade_intervals,rwidth=0.7,facecolor="pink")
plt.xticks([0,40,70,100])
plt.xlabel("Percentage")
plt.ylabel("No of Stodents")
plt.show()
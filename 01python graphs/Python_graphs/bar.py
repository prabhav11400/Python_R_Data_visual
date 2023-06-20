from matplotlib import pyplot as plt
x=["2016","2017","2018","2019","2020","2021"]
y=[256,305,354,276,378,398]
c=["red","pink","purple","orange","blue","green"]
plt.bar(x,y,color=c,width=0.4)
plt.xlabel("Year")
plt.ylabel("No of Students placed out of 400 students")
plt.show()
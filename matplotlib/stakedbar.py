from matplotlib import pyplot as plt
years=["2016","2017","2018","2019","2020"]
#y=[256,305,354,276,378,398]
placements=[150,275,324,290,375]
c=["red","pink","purple","orange","blue"]
#plt.bar(x,y,color=c,width=0.4)
cse=[75,80,47,82,90]
it=[46,58,35,53,62]
ece=[67,59,72,62,67]
eee=[10,20,30,40,50]
ece_start=[cse[i]+it[i] for i  in range(len(cse))] #since i for cse is always greater than i for it in this case
eee_start=[ece_start[i]+ece[i] for i in range(len(ece))]
plt.title("Placement Comparison")
plt.bar(years,cse,width=0.4,color="red",label="CSE")
plt.bar(years,it,width=0.4,bottom=cse,color="green",label="IT")
plt.bar(years,ece,width=0.4,bottom=ece_start,color="yellow",label="ECE")
plt.bar(years,eee,width=0.4,bottom=eee_start,color="blue",label="EEE")
plt.xlabel("Year")
plt.ylabel("No of Students placed out of 300 students")
plt.ylim(0,300)
plt.legend()
plt.show()

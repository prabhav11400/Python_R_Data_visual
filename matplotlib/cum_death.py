from matplotlib import pyplot as plt 
import numpy as np 
import pandas
df=pandas.read_csv("covid19.csv")
x=[]
y=[]
ln=len(df["Country_code"])
for i in range(ln):
    if(df["Country_code"][i]=="IN"):
        x.append(df["Date_reported"][i])
        y.append(df["Cumulative_deaths"][i])
        
        
        
       
     #   plt.plot(x,y)

#plt.plot(x,y)
plt.bar(x,y)
plt.show()
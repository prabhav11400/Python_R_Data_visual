from matplotlib import pyplot as plt
import numpy as np;
import pandas

df = pandas.read_csv("covid19.csv")
x=[]
y = []

ln = len(df["Country_code"])

for i in range(ln):
    if (df["Country_code"][i] == "IN"):
        # x.append(df["Date_reported"][i])
        y.append(df["New_cases"][i])

x = [i for i in range(1, len(y)+1)]
# y2 = [y[0]]
# for i in range(1, len(y)):
#     y2.append(y2[-1]+y[i])
        
        

print(x, y)
#plt.xticks([i for i in range(0, 1000, 50)])
plt.bar(x, y)
# plt.plot(x, y2)
plt.show()

# x=np.arange(0,10,2)
# y=x**2
# plt.plot(x,y,marker="*",ms="20",mec="k",mfc="b")
# plt.show()

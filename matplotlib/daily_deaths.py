from matplotlib import pyplot as plt
import numpy as np;
import pandas

df = pandas.read_csv("covid19.csv")

x = []
y = []

ln = len(df["Country_code"])

for i in range(ln):
    if (df["Country_code"][i] == "IN"):
        x.append(df["Date_reported"][i])
        y.append(df["New_deaths"][i])
plt.xlabel("Date")
plt.ylabel("Daily_Deaths due to covid19 in india")
# print(x, y)
plt.bar(x, y)
plt.plot(x,y)
plt.show()


# x=np.arange(0,10,2)
# y=x**2
# plt.plot(x,y,marker="*",ms="20",mec="k",mfc="b")
# plt.show()

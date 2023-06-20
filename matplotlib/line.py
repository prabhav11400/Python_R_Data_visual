from matplotlib import pyplot as plt
import numpy as np;
import pandas as pd
d=np.loadtxt("covid19.csv",dtype=float)
#df=pd.read_csv("covid19.csv")
# d = pd.read_csv("C:\\Users\\prabh\\OneDrive\\Documents\\Excel Files\\mess.csv")
df=pd.DataFrame(d)
print(df.head())
# print(df.columns)
# print(df.head())
# print(df.head(7))
# print(df.tail())
# print(df.tail(3))
# print(df.describe())
# print(df.columns)
# print(df['Roll No'])
# print(df[['Roll No','go']])
# print(df[['Roll No','go']].head())
# print(df[['Roll No','go']].head(10))
# print(df[1:10])
# print(df[1:10:2])
# print(df[1:10:5])
# print(df[['Roll No','Name','Marks']][1:6])
# print(df[['Roll No','Name','Marks']][:6])
# print(df[['Roll No','Name','Marks']][3:])
# print(df.loc[1])
# print(df.loc[1:6])

# for index,rows in df.iterrows():
#     print(index,rows)

# for index,rows in df.iterrows():
#     print(index,rows[['Roll No','Name','Marks']])

# print(df.loc[df['Roll No']=='pH22mscst11036'])
# print(df.loc[df['Marks']==70])

x = []
y = []

ln = len(df["Country_code"])

for i in range(ln):
    if (df["Country_code"][i] == "IN"):
        x.append(df["Date_reported"][i])
        y.append(df["New_cases"][i])

# print(x, y)
# plt.bar(x, y)
plt.plot(x,y)
plt.show()


# # x=np.arange(0,10,2)
# # y=x**2
# # plt.plot(x,y,marker="*",ms="20",mec="k",mfc="b")
# # plt.show()


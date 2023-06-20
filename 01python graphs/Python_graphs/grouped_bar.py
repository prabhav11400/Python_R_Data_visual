from matplotlib import pyplot as plt
import numpy as np
#import pandas

#df: pandas.DataFrame=pandas.read_fwf("medals.txt", header=None)
# print(df)
arr = np.loadtxt('medals.txt',dtype='int')

years=["2017", "2018"," 2019","2020"]
# cse=arr[0]
# it=arr[1]
# ece=arr[2]
# eee=arr[3]

# for i in range(4):
#     cse[i] = arr[i]
#     it[i] = arr[4+i]
#     ece[i] = arr[8+i]
#     eee[i] = arr[12+i]
#print(cse)
w=0.2;
plt.figure(figsize=(10,5))
cse_bar=np.arange(len(years))
it_bar=[i+w for i in cse_bar ]
ece_bar=[i+w for i in it_bar ]
eee_bar=[i+w for i in ece_bar ]

plt.bar(cse_bar,arr[0,:],width=w,label="cse")
plt.bar(it_bar,arr[1,:],width=w,label="it")
plt.bar(ece_bar,arr[2,:],width=w,label="ece")
plt.bar(eee_bar,arr[3,:],width=w,label="eee")

plt.xticks((cse_bar+w+w/2),years)
plt.ylim(0,200)
plt.title("Placement Comparison")
plt.xlabel("YEARS")
plt.ylabel("PLACEMENT COUNT")
plt.legend()
plt.show()


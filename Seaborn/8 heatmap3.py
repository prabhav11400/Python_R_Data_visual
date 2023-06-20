import numpy as np
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt
var1=np.linspace(1,10,10).reshape(2,5)
# v=sns.heatmap(var1,cmap='PuOr',annot=True)
arr=np.array([['a0','a1','a2','a3','a4'],
               ['a5','a6','a7','a8','a9']])
# v=sns.heatmap(var1,cmap='PuOr',annot=arr,fmt='s')
# v=sns.heatmap(var1,cmap='PuOr',annot=arr,fmt='s',linewidth=10,linecolor='r',cbar=False,xticklabels=False,yticklabels=False)
v=sns.heatmap(var1,cmap='PuOr',annot=arr,fmt='s',linewidth=10,linecolor='r',cbar=False,xticklabels=False,yticklabels=False)
v.set(xlabel='python',ylabel="AAMN")
sns.set(font_scale=5)
plt.show()
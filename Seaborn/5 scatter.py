import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
var=sns.load_dataset("penguins")
# print(var)
# sns.scatterplot(x="bill_length_mm",y="bill_depth_mm",data=var)
# sns.scatterplot(x="bill_length_mm",y="bill_depth_mm",data=var,style='sex')
# sns.scatterplot(x="bill_length_mm",y="bill_depth_mm",data=var,style='sex',hue='sex')
sns.scatterplot(x="bill_length_mm",y="bill_depth_mm",data=var,style='sex',hue='sex',sizes=(100,50),palette='gist_ncar',alpha=0.7)
plt.show()
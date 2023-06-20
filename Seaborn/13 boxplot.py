import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
var=sns.load_dataset("tips")
sns.set(style="whitegrid")
# sns.boxplot(x="day",y="total_bill",data=var,hue="time")
# sns.boxplot(x="day",y="total_bill",data=var,hue="time",color="g")
# sns.boxplot(x="day",y="total_bill",data=var,hue="sex",color="g")
# sns.boxplot(x="day",y="total_bill",data=var,hue="sex",color="r",showmeans=True)
# sns.boxplot(x="day",y="total_bill",data=var,hue="sex",color="r",showmeans=True,order=['Fri','Sun','Thur','Sat'],hue_order=['Female','Male'])
# sns.boxplot(x="day",y="total_bill",data=var,hue="sex",color="r",showmeans=True,order=['Fri','Sun','Thur','Sat'],hue_order=['Female','Male'],orient="v")
# sns.boxplot(x="day",y="total_bill",data=var,hue="sex",color="r",showmeans=True,order=['Fri','Sun','Thur','Sat'],hue_order=['Female','Male'],orient="v")
# sns.boxplot(data=var,orient='h') # ye sabhi numerical columns ke horizontal box plot ko banakar de dega
# sns.boxplot(data=var,orient='v')# ye sabhi numerical columns ko varticle box plot me banakar de dega

# boxplot of single column
# sns.boxplot(x=var['total_bill']) # horizontal bar plot
sns.boxplot(y=var['total_bill']) # vertical bar plot
plt.show()
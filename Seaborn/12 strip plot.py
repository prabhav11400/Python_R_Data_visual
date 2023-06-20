import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset("tips")
# sns.stripplot(x="day",y="total_bill",data=df)
# sns.stripplot(x="day",y="total_bill",data=df,hue="sex")
# sns.stripplot(x="day",y="total_bill",data=df,hue="sex",palette="rocket_r")
# sns.stripplot(x="day",y="total_bill",data=df,hue="sex",palette="rocket_r",linewidth=1)
# sns.stripplot(x="day",y="total_bill",data=df,hue="sex",palette="rocket_r",linewidth=1,edgecolor="r")
# sns.stripplot(x="day",y="total_bill",data=df,hue="sex",palette="rocket_r",linewidth=1,edgecolor="r",size=10)
# sns.stripplot(x="day",y="total_bill",data=df,hue="sex",palette="rocket_r",linewidth=1,edgecolor="r",size=10)
# sns.stripplot(x=df["total_bill"])
sns.stripplot(y=df["total_bill"])
plt.show()
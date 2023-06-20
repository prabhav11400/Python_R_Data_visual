import matplotlib.pyplot as plt
import seaborn as sns

var =sns.load_dataset("tips").head(20)
print(var)
# sns.pairplot(var,hue="sex")
# sns.pairplot(var,hue="sex",vars=['total_bill',"tip"])
# sns.pairplot(var,hue="sex",vars=['total_bill',"tip"],palette="BuGn")
# sns.pairplot(var,hue="sex",x_vars=['total_bill',"tip"],palette="BuGn")
# sns.pairplot(var,hue="sex",y_vars=['total_bill',"tip"],palette="BuGn")
# sns.pairplot(var,hue="sex",y_vars=['total_bill',"tip"],palette="BuGn",kind='reg')
# sns.pairplot(var,hue="sex",y_vars=['total_bill',"tip"],palette="BuGn",kind='kde')
sns.pairplot(var,hue="sex",y_vars=['total_bill',"tip"],palette="BuGn",kind='kde',diag_kind="hist")
plt.show()
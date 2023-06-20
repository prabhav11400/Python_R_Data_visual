import matplotlib.pyplot as plt
import seaborn as sns
var=sns.load_dataset("tips")
# print(var)
# sns.catplot(x="day",y="size",data=var,hue="sex",palette="winter",kind="boxen")
sns.catplot(x="day",y="size",data=var,hue="sex",palette="winter",kind="box")
plt.show()
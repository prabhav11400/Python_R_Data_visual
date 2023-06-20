import seaborn as sns
import matplotlib.pyplot as plt
var=sns.load_dataset("tips")
# fg=sns.FacetGrid(var,col="sex",hue="day") # different graps based on col or sex column
fg=sns.FacetGrid(var,col="sex",hue="day") 
# fg.map(plt.scatter,"total_bill","tip").add_legend() # legend hue or day pr lagega.
# fg.map(plt.bar,"total_bill","tip",edgecolor="r").add_legend()
# fg.map(plt.boxplot,"total_bill","tip").add_legend()
plt.show()
import seaborn as sns
import matplotlib.pyplot as plt
# import pandas as pd
f=sns.load_dataset('tips')
# print(f)
# sns.violinplot(x="day",y="total_bill",data=f,hue="smoker")
sns.violinplot(x="day",y="total_bill",data=f,hue="smoker",inner="quartile")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
var=sns.load_dataset('tips')
# print(var)
# sns.countplot(x='sex',data=var)
# sns.countplot(x='sex',data=var,hue="smoker")
# sns.countplot(y='sex',data=var,hue="smoker")
# sns.countplot(x='sex',data=var,hue="smoker",color="r")
sns.countplot(x='sex',data=var,hue="smoker",color="r",saturation=0.5)
plt.show()

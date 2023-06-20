import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df=sns.load_dataset('anagrams')
dff=df.drop(columns=['attnr'],axis=1).head(10)
sns.heatmap(dff)
plt.show()
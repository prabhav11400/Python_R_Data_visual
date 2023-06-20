import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df=sns.load_dataset('penguins')
# print(df)
sns.displot(df['bill_length_mm'])
plt.show()
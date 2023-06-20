import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('penguins')
sns.barplot(x=df.island,y=df.bill_length_mm)
plt.show()
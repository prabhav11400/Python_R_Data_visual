import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df=np.linspace(1,10,20).reshape(4,5)
sns.heatmap(df)
print(df)
plt.show()
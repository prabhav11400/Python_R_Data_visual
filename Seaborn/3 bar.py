import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

var=sns.load_dataset("penguins")
# sns.barplot(x='island',y="bill_length_mm",data=var,hue="sex",hue_order=['Female','Male'])
order1=['Biscoe','Dream','Torgersen']
sns.barplot(x='island',y="bill_length_mm",data=var,hue="sex",order=order1,hue_order=['Female','Male'])
plt.show()
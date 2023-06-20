import seaborn as sns
import matplotlib.pyplot as plt
y1=sns.load_dataset("penguins")
print(y1)
# sns.lineplot(x="bill_length_mm",y="flipper_length_mm",data=y1)
# sns.lineplot(x="bill_length_mm",y="bill_depth_mm",data=y1,hue="sex")
# sns.lineplot(x="bill_length_mm",y="bill_depth_mm",data=y1,hue="sex",size=50)
# sns.lineplot(x="bill_length_mm",y="bill_depth_mm",data=y1,hue="sex",style="sex")
sns.lineplot(x="bill_length_mm",y="bill_depth_mm",data=y1,hue="sex",palette='Accent')

plt.show()
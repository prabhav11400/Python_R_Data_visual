#REMEMBER,This is not a stacked bar plot .This is 3 bar plots at same bars.And best for this situation
#  we can eaily see out of total confirmed cases ,died and recovered cases too.
# # OVERLAPPING bar plots 


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
data = pd.read_csv('district.csv')
# data.head()
print(data)
 
re=data.iloc[:20,5].values # index=5 ke column ki firt 20 entities
de=data.iloc[:20,4].values
co=data.iloc[:20,3].values 
x=list(data.iloc[:20,0]) # i.e. 0th index ke column ki first 20 entities ko x namak list variable me store kr do(list= comma seperated arrar)
# print(x)
plt.figure(figsize=(10,10))
ax=plt.axes()
 
ax.set_facecolor('black')
ax.grid(linewidth=0.4, color='blue')
 
 
plt.xticks(rotation='vertical',
           size='10',
           color='black')#ticks of X
 
plt.yticks(size='10',color='black')
 
 
ax.set_xlabel('\nDistrict',size=20,
              color='green')
ax.set_ylabel('No. of cases\n',size=20,
              color='red')
 
 
plt.tick_params(size=5,color='black')
 
 
ax.set_title('Maharashtra District wise breakdown\n',
             size=20,color='Black')
 
plt.bar(x,co,label='re')
plt.bar(x,re,label='re',color='green')
plt.bar(x,de,label='re',color='red')
 
for i,j in zip(x,co):
    ax.annotate(str(int(j)),
                xy=(i,j+3),
                color='Yellow',
                size='5')

plt.legend(['Confirmed','Recovered','Deceased'],
           fontsize=10)
plt.show()
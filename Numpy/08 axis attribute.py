import numpy as np
a=np.array([[40,20,30],[90,30,10]])
print(a)
a=np.sort(a,axis=0)# changing in a itself column wise uper se neeche increasing order
print(a)
a=np.sort(a,axis=1)# sorting in the latest a itself rowwise increasing order
print(a)
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

d = np.loadtxt("time_zpos_in_water_run2.dat",dtype='double')
df=pd.DataFrame(d)
print(df.describe())


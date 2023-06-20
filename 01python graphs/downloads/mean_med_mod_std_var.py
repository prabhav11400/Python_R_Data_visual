from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

d = np.loadtxt("time_zpos_in_water_run2.dat",dtype='double')
df=pd.DataFrame(d)
# print(df.mean())
# print(df.median())
#print(df.round(2).mode()) # for ronding each values to 2 decimal places and then get mode .May be no mode for any row,epending upon no repeating element
#print(df.std())
# print(df.var())




#for single column
# print(df[0].mean())
# print(df[1].mean())
# print(df[2].mean())
# print(df[1].median())
# print(df[2].median())
# print(df[0].median())
# print(df[1].mode())
# print(df[2].mode())
# print(df[0].std())
# print(df[1].std())
# print(df[2].std())
# print(df[0].var())
# print(df[1].var())
# print(df[2].var())
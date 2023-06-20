import csv
import matplotlib as plt
import pandas as pd
df = pd.read_csv('covid19.csv',delimiter=',')
data = [tuple(x) for x in df.values]

print(data)
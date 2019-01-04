import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print(df)

print("----返回所请求轴的值的总和。 默认情况下，轴为索引(axis=0)----")
print(df.sum())

print("----mean()----")
print(df.mean())

print("----std()----")
print(df.std())

print("----describe()函数是用来计算有关DataFrame列的统计信息的摘要----")
print(df.describe())

print(df. describe(include='all'))
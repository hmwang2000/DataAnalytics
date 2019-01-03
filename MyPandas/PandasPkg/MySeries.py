#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)

data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print(s)

data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print(s)

data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print(s)

s = pd.Series(5, index=[0, 1, 2, 3])
print(s)

s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s[0])
print(s[:3])
print(s[-3:])
print(s['a'])
print(s[['a','c','e']])



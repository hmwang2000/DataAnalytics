import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
index = pd.date_range('1/1/2020', periods=10),
columns = ['A', 'B', 'C', 'D'])

print("-----------.rolling()函数-------------")
print (df.rolling(window=3).mean())

print("-----------.expanding()函数-------------")
print (df.expanding(min_periods=3).mean())

print("-----------.ewm()函数-------------")
#ewm()可应用于系列数据。指定com，span，halflife参数，并在其上应用适当的统计函数。它以指数形式分配权重
print (df.ewm(com=0.5).mean())
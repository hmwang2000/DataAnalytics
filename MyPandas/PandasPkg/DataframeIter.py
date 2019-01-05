import pandas as pd
import numpy as np

N=20

df = pd.DataFrame({
    'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
    'x': np.linspace(0,stop=N-1,num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low','Medium','High'],N).tolist(),
    'D': np.random.normal(100, 10, size=(N)).tolist()
    })

print(df)
print("-----------迭代DataFrame提供列名------------")
for col in df:
   print (col)

'''
要遍历数据帧(DataFrame)中的行，可以使用以下函数 -
    iteritems() - 迭代(key，value)对
    iterrows() - 将行迭代为(索引，系列)对
    itertuples() - 以namedtuples的形式迭代行
'''

print("-----------iteritems()------------")
#将每个列作为键，将值与值作为键和列值迭代为Series对象
df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
for key,value in df.iteritems():
   print (key,value)

print("-----------iterrows()------------")
#iterrows()返回迭代器，产生每个索引值以及包含每行数据的序列
df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])
for row_index,row in df.iterrows():
   print (row_index,row)

print("-----------itertuples()------------")
#itertuples()方法将为DataFrame中的每一行返回一个产生一个命名元组的迭代器。
# 元组的第一个元素将是行的相应索引值，而剩余的值是行值
df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])
for row in df.itertuples():
    print (row)

#不要尝试在迭代时修改任何对象。迭代是用于读取，迭代器返回原始对象(视图)的副本，
# 因此更改将不会反映在原始对象上。
df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])

for index, row in df.iterrows():
   row['a'] = 10
print (df)

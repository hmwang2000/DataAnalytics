import pandas as pd
import numpy as np

#https://www.yiibai.com/pandas/python_pandas_quick_start.html

s = pd.Series([1,3,5,np.nan,6,8])

print(s)

#通过传递numpy数组，使用datetime索引和标记列来创建DataFrame
dates = pd.date_range('20190101', periods=7)
print(dates)

print("--"*32)

df0 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20190202'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })

print(df0)

print("--"*32)
df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
print(df)

#显示索引，列和底层numpy数据
print("index is :" )
print(df.index)
print("columns is :" )
print(df.columns)
print("values is :" )
print(df.values)

#描述显示数据的快速统计摘要
print(df.describe())

#调换数据
dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df.T)

#轴排序
print(df.sort_index(axis=1, ascending=False))

#按值排序
dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df.sort_values(by='B'))

#选择一列，产生一个系列
print(df['A'])
print(df.A)

#选择通过[]操作符，选择切片行
print(df[0:3])
print("========= 指定选择日期 ========")
print(df['20170102':'20170103'])

#按标签选择
print(df.loc['20170102':'20170104',['A','B']])

#通过位置选择
print(df.iloc[3:5,0:2])
print(df.iloc[[1,2,4],[0,2]])
print(df.iloc[1:3,:])
print(df.iloc[:,1:3])
print(df.iloc[1,1])

#布尔索引
print(df[df.A > 0])  #使用单列的值来选择数据
print(df[df > 0])  #DataFrame中选择值

#使用isin()方法进行过滤
df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']
print(df2)
print("============= start to filter =============== ")
print(df2[df2['E'].isin(['two','four'])])

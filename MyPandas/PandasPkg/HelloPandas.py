import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 数据可视化必须的模块

data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list("ABCD"))
# 创建一个1000X4矩阵，设置索引,定义了4个列属性
data = data.cumsum()

# 在图上打印出点的数据,用scatter,如指定A和B属性分别为x和y
ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label='Class 1')
data.plot.scatter(x='A', y='C', color='DarkGreen', label='Class 2', ax=ax)
# ax=ax表示下面这行绿色的组数据我们也想附在ax这张图里
plt.show()
# 打印出的图类型还有很多，如bar、hist、box、kde、area、scatter、hexbin、pie，可以自己试试

data1 = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list("ABCD"))
# 创建一个1000X4矩阵，设置索引,定义了4个列属性
data1 = data1.cumsum()
print(data1.head())
# 打印矩阵前5个数据（5是默认个数）
data1.plot()
plt.show()

dates = pd.date_range('20180101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
# 我们创建一个DataFrame，里面包含一个二维的numpy数组，行索引用刚才创建的dates，列索引定义为a,b,c,d
df.iloc[2, 2] = 1111
# 用行号和列号修改指定位置的元素的值
print(df)
df.loc['20180101', 'B'] = 2222
# 用标签修改指定位置的元素的值
print(df)
# df[df.A > 0] = 0
# # A>0的行的所有元素都改成0
# print(df)
df.A[df.A > 4] = 0
# A>4的项的A值全改成0
print(df)
df['F'] = np.nan
# 添加一列F
print(df)
df['G']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20180101',periods=6))
# 添加一个不是空值的列,添加的值为1到6，index和原有的一样
print(df)
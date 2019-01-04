import pandas as pd
import numpy as np

'''
重新索引会更改DataFrame的行标签和列标签。重新索引意味着符合数据以匹配特定轴上的一组给定的标签。
可以通过索引来实现多个操作 -
    重新排序现有数据以匹配一组新的标签。
    在没有标签数据的标签位置插入缺失值(NA)标记。
'''
N=20

df = pd.DataFrame({
   'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   'x': np.linspace(0,stop=N-1,num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
})
print (df)

#reindex the DataFrame
df_reindexed = df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])
print (df_reindexed)

print("----------重建索引与其他对象对齐------------")
df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])

df1 = df1.reindex_like(df2)
print(df1)

print("----------填充时重新加注------------")
df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])

# Padding NAN's
print(df2.reindex_like(df1))

# Now Fill the NAN's with preceding Values
print ("Data Frame with Forward Fill:")
print(df2.reindex_like(df1,method='ffill'))

print("----------重建索引时的填充限制------------")
df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])

# Padding NAN's
print(df2.reindex_like(df1))

# Now Fill the NAN's with preceding Values
print ("Data Frame with Forward Fill limiting to 1:")
print(df2.reindex_like(df1,method='ffill',limit=1))

print("----------重命名------------")
df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
print(df1)

print ("After renaming the rows and columns:")
print(df1.rename(columns={'col1' : 'c1', 'col2' : 'c2', 'col3' : 'c3'},index = {0 : 'apple', 1 : 'banana', 2 : 'durian'}))


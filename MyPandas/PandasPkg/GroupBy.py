import pandas as pd
import numpy as np

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

print (df)

print (df.groupby('Team').groups)
print (df.groupby(['Team','Year']).groups)

print("-------------迭代遍历分组-----------------")
#使用groupby对象，可以遍历类似itertools.obj的对象
grouped = df.groupby('Year')
for name,group in grouped:
    print (name)
    print (group)

print("-------------选择一个分组-----------------")
print (grouped.get_group(2014))

print("-------------聚合-----------------")
# 聚合函数为每个组返回单个聚合值。当创建了分组(group by)对象，就可以对分组数据执行多个聚合操作。
#一个比较常用的是通过聚合或等效的agg方法聚合
print (grouped['Points'].agg(np.mean))
print (grouped.agg(np.size))

print("-------------一次应用多个聚合函数-----------------")
grouped = df.groupby('Team')
agg = grouped['Points'].agg([np.sum, np.mean, np.std])
print (agg)

print("-------------转换-----------------")
#分组或列上的转换返回索引大小与被分组的索引相同的对象
grouped = df.groupby('Team')
score = lambda x: (x - x.mean()) / x.std()*10
print (grouped.transform(score))

print("-------------过滤-----------------")
#过滤根据定义的标准过滤数据并返回数据的子集。filter()函数用于过滤数据
filter = df.groupby('Team').filter(lambda x: len(x) >= 3)
print (filter)
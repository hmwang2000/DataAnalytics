'''
Pandas有两种排序方式，它们分别是 -
    按标签
    按实际值
'''

import pandas as pd
import numpy as np

unsorted_df=pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns=['col2','col1'])
print (unsorted_df)

print("-----------按标签排序------------")
sorted_df=unsorted_df.sort_index()
print (sorted_df)

print("-----------排序顺序------------")
sorted_df = unsorted_df.sort_index(ascending=False)
print (sorted_df)

print("-----------按列排列------------")
sorted_df=unsorted_df.sort_index(axis=1)
print (sorted_df)

print("-----------按值排序------------")
unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
sorted_df = unsorted_df.sort_values(by='col1')
print (sorted_df)

print("-----------排序算法------------")
#sort_values()提供了从mergeesort，heapsort和quicksort中选择算法的一个配置。Mergesort是唯一稳定的算法
unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
sorted_df = unsorted_df.sort_values(by='col1' ,kind='mergesort')
print (sorted_df)
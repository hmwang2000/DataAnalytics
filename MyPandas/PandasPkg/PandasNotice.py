import pandas as pd
import numpy as np

#ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
#if pd.Series([False, True, False]):
#    print ('I am True')

if pd.Series([False, True, False]).any():
    print("I am any")

print("--------------------按位布尔值-----------------------")
s = pd.Series(range(5))
print (s==4)

s = pd.Series(list('abc'))
s = s.isin(['a', 'c', 'e'])
print (s)

'''
.ix is deprecated. Please use
.loc for label based indexing or
.iloc for positional indexing
'''
print("--------------------重构索引与ix陷阱-----------------------")
df = pd.DataFrame(np.random.randn(6, 4), columns=['one', 'two', 'three',
'four'],index=list('abcdef'))

print (df)
print ("=============================================")
print (df.ix[['b', 'c', 'e']])
#等同于 print (df.reindex(['b', 'c', 'e']))

#有人可能会得出这样的结论，ix和reindex是基于这个100％的等价物。 除了整数索引的情况，它是true
df = pd.DataFrame(np.random.randn(6, 4), columns=['one', 'two', 'three',
'four'],index=list('abcdef'))

print (df)
print("=====================================")
print (df.ix[[1, 2, 4]])
print("=====================================")
print (df.reindex([1, 2, 4]))
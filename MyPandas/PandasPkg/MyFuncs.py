import pandas as pd
import numpy as np

def adder(ele1,ele2):
   return ele1+ele2

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.pipe(adder,2)
print(df)

print("---------行或列智能函数应用----------")
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
print(df)
df.apply(np.mean)
print(df)

print("---------元素智能函数应用----------")
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
print(df)
df.applymap(lambda x:x*100)
print(df)


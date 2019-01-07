import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#基本绘图：绘图
#Series和DataFrame上的这个功能只是使用matplotlib库的plot()方法的简单包装实现

df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('2018/12/18',
   periods=10), columns=list('ABCD'))

df.plot()
plt.show()

'''
绘图方法允许除默认线图之外的少数绘图样式。 这些方法可以作为plot()的kind关键字参数提供。这些包括 -
    bar或barh为条形
    hist为直方图
    boxplot为盒型图
    area为“面积”
    scatter为散点图
'''
print("-------------条形图--------------")
df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df.plot.bar()
plt.show()

print("-------------堆积条形图--------------")
df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df.plot.bar(stacked=True)
plt.show()

print("-------------直方图--------------")
df = pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':
np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])
df.plot.hist(bins=20)
plt.show()

df=pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':
np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])
df.hist(bins=20)
plt.show()

print("-------------箱型图--------------")
df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
df.plot.box()
plt.show()

print("-------------饼状图--------------")
df = pd.DataFrame(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])
df.plot.pie(subplots=True)
plt.show()

print("-------------饼状图--------------")
df = pd.DataFrame(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])
df.plot.pie(subplots=True)
plt.show()

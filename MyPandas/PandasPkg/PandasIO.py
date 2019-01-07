import pandas as pd

# 自定义索引
# 可以指定csv文件中的一列来使用index_col定制索引
df=pd.read_csv("D:\\DevSpace\\DataSamples\\temp.csv",index_col=['S.No'])
print (df)

# header_names
# 使用names参数指定标题的名称
df=pd.read_csv("D:\\DevSpace\\DataSamples\\temp.csv", names=['a', 'b', 'c','d','e'])
print (df)

# 使用header参数来删除文件中的标题
print("-------------header=0--------------")
df=pd.read_csv("D:\\DevSpace\\DataSamples\\temp.csv",names=['a','b','c','d','e'],header=0)
print (df)

# skiprows跳过指定的行数
print("-------------skiprows--------------")
df=pd.read_csv("D:\\DevSpace\\DataSamples\\temp.csv", skiprows=2)
print (df)

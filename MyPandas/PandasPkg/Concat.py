import pandas as pd

one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
print("-------------------------------------------")
print(one)
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
print("-------------------------------------------")
print(two)

print("-------------------------------------------")
rs = pd.concat([one,two])
print(rs)

print("-------------------ignore_index=True------------------------")
rs = pd.concat([one,two],keys=['x','y'],ignore_index=True)
print(rs)

print("--------------------Axis=1-----------------------")
rs = pd.concat([one,two],axis=1)
print(rs)

# 使用附加连接
# 连接的一个有用的快捷方式是在Series和DataFrame实例的append方法。
# 这些方法实际上早于concat()方法。 它们沿axis=0连接，即索引
# rs = one.append([two,one,two])



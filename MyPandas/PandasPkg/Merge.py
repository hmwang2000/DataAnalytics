import pandas as pd

left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print (left)
print("========================================")
print (right)
print("========================================")
rs = pd.merge(left,right,on='id')
print(rs)
print("========================================")
rs = pd.merge(left,right,on=['id','subject_id'])
print(rs)

print("==================Left Join======================")
rs = pd.merge(left, right, on='subject_id', how='left')
print (rs)
print("==================Right Join======================")
rs = pd.merge(left, right, on='subject_id', how='right')
print(rs)
print("==================Outer Join======================")
rs = pd.merge(left, right, how='outer', on='subject_id')
print (rs)
print("==================Inner Join======================")
rs = pd.merge(left, right, how='inner', on='subject_id')
print (rs)

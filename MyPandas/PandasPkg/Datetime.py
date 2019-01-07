from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('D:\\DevSpace\\DataSamples\\stock.csv')
df = pd.DataFrame(data, columns = ['ValueDate', 'Price'])

# Set the Date as Index
df['ValueDate'] = pd.to_datetime(df['ValueDate'])
df.index = df['ValueDate']
del df['ValueDate']


df.plot(figsize=(15, 6))
plt.show()

print("--------------------datetime.now()用于获取当前的日期和时间----------------------")
print(pd.datetime.now())

print("--------------------创建一个时间戳----------------------")
time = pd.Timestamp('2019-02-01')
print(time)

print("--------------------创建一个时间范围----------------------")
time = pd.date_range("12:00", "23:59", freq="30min").time
print(time)

print("--------------------改变时间的频率----------------------")
time = pd.date_range("12:00", "23:59", freq="H").time
print(time)

print("--------------------转换为时间戳----------------------")
time = pd.to_datetime(pd.Series(['Jul 31, 2009','2019-10-10', None]))
print(time)

time = pd.to_datetime(['2009/11/23', '2019.12.31', None])
print(time)

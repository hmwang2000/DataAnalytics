import pandas as pd
import numpy as np

data = np.random.randint(1, 10, (5, 3, 2))
'''
pnl = pd.Panel(
    data,
    items=['item {}'.format(i) for i in range(1, 6)],
    major_axis=[2015, 2016, 2017],
    minor_axis=['US', 'UK']
)
print(pnl)

#DeprecationWarning: Panel is deprecated and will be removed in a future version. 
#The recommended way to represent these types of 3-dimensional data are with a MultiIndex 
#on a DataFrame, via the Panel.to_frame() method. Alternatively, you can use the xarray 
#package http://xarray.pydata.org/en/stable/. Pandas provides a .to_xarray() method to 
#help automate this conversion.
'''

print("------------------------3-dimensional data---------------------------------")
data = data.reshape(5, 6).T
df = pd.DataFrame(
    data=data,
    index=pd.MultiIndex.from_product([[2015, 2016, 2017], ['US', 'UK']]),
    columns=['item {}'.format(i) for i in range(1, 6)]
)
print(df)

print("------------------------4-dimensional data---------------------------------")
data = np.random.randint(1, 100, (5, 3, 4))
data = data.reshape(5, 12).T
df = pd.DataFrame(
    data=data,
    index=pd.MultiIndex.from_product([[2015, 2016, 2017], ['US', 'UK'],['Jan', 'Feb']]),
    columns=['item {}'.format(i) for i in range(1, 6)]
)
print(df)

print("------------------------df['item 1']---------------------------------")
print(df['item 1'])
print("------------------------df['item 1'].unstack()---------------------------------")
print(df['item 1'].unstack())
print("------------------------df.xs(2015)---------------------------------")
print(df.xs(2015))
print("------------------------df.xs('US',level=1)---------------------------------")
print(df.xs('US', level=1))
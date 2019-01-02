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

data = data.reshape(5, 6).T
df = pd.DataFrame(
    data=data,
    index=pd.MultiIndex.from_product([[2015, 2016, 2017], ['US', 'UK']]),
    columns=['item {}'.format(i) for i in range(1, 6)]
)
print(df)
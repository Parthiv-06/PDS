import os
import pandas as pd
import numpy as np

data_csv=pd.read_csv('D:\\spyder_file_reading\\Toyota.csv',index_col=0,na_values=['??','????'])
print(data_csv.dtypes)
print(data_csv.select_dtypes(exclude='int64'))
print(data_csv.info())
print(np.unique(data_csv['KM']))
data_csv['Automatic']=data_csv['Automatic'].astype('object')
print(data_csv.dtypes)
data_csv['Doors'].replace('three',3,inplace=True)
print(data_csv.isnull().sum())
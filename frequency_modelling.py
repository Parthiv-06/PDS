import os
import pandas as pd
import numpy as np

data_csv=pd.read_csv('D:\\spyder_file_reading\\Toyota.csv',index_col=0,na_values=['??','????'])
print(pd.crosstab(index=data_csv['FuelType'],columns='count',dropna=True))
print(pd.crosstab(index=data_csv['FuelType'],columns=data_csv['Automatic'],dropna=True))
print(pd.crosstab(index=data_csv['FuelType'],columns=data_csv['Automatic'],dropna=True,normalize=True))
print(pd.crosstab(index=data_csv['FuelType'],columns=data_csv['Automatic'],dropna=True,normalize=True,margins=True))
print(pd.crosstab(index=data_csv['FuelType'],columns=data_csv['Automatic'],dropna=True,normalize='index',margins=True))
print(pd.crosstab(index=data_csv['FuelType'],columns=data_csv['Automatic'],dropna=True,normalize='columns',margins=True))
numerical_data=data_csv.select_dtypes(exclude=['object'])
print(numerical_data)
print(numerical_data.corr())
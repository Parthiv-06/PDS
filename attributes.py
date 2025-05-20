"""attributes"""
import os 
import pandas as pd
import numpy as np
 
data_csv=pd.read_csv('D:\\spyder_file_reading\\Toyota.csv',index_col=0,na_values=['??','????'])
print(data_csv.index)
print(data_csv.columns)
print(data_csv.size)
print(data_csv.shape)
print(data_csv.ndim)
print(data_csv.memory_usage())
print(data_csv.head(5))
print(data_csv.tail(5))
print(data_csv.at[3,'Price'])
print(data_csv.iat[3,4])
print(data_csv.loc[:,'Price'])
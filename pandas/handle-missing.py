#!/bin/python

import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [28, 22, np.nan, 35, 29],
    'Department': ['HR', np.nan, 'IT', 'HR', 'Finance'],
    'Salary': [55000, 60000, 65000, np.nan, 70000],
    'City': ['New York',np.nan, 'Chicago', 'Raleigh', 'New York']
}

df = pd.DataFrame(data)
print(df)
print()

print("Missing data:")
print(df.isna())
print()
print("Drop Rows with Missing Data:")
print(df.dropna())
print()
print("Drop Cols with Missing Data:")
print(df.dropna(axis=1))
print()
print("Filling Missing Data:")
print(df.fillna({'Age': df['Age'].mean(), 'Department': 'Unknown', 'Salary': df['Salary'].mean(), 'City': 'Unknown'}))
print()
print("Interpolating Missing Data:(for numbers data field)")
print(df.interpolate())
print()

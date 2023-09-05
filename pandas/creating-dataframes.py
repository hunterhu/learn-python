#!/bin/python

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25,30,22]
}
df = pd.DataFrame(data)
print(df)

print("Accessing Columns...")
print(df['Name'])
print(df['Age'])

print("Accessing Rows by index(iloc: integer location)...")
print(df.iloc[0])

print("Accessing rows by label...")
print(df.loc[0])

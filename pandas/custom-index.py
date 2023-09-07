#!/bin/python

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25,30,22]
}

custom_index = ['A', 'B', 'C']

df = pd.DataFrame(data, index=custom_index)

print(df)

#by integer index
print(df.iloc[0])
#by label
print(df.loc['B'])
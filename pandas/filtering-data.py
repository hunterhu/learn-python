#!/bin/python

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [28, 22, 30, 35, 29],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance'],
    'Salary': [55000, 60000, 65000, 58000, 70000]
}

df = pd.DataFrame(data)

print(df)
print()
print(df[(df['Age'] > 25) & (df['Department'] == 'IT')])
print()
print(df[(df['Age'] > 30) | (df['Department'] == 'Finance')])
print()
print(df[(df['Name'].str.contains('a', case=False))])
print()
print(df[df['Age'].isin([22, 30])])
print()
print(df[((df['Age'] > 25) & (df['Department'] == 'IT')) | (df['Department'] == 'Finance')])
print()
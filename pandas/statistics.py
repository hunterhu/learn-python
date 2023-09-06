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

print(df['Age'].mean())
print(df['Age'].median())
print(df['Age'].max())
print(df['Age'].min())

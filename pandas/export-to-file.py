#!/bin/python

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [28, 22, 25, 35, 29],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance'],
    'Salary': [55000, 60000, 65000, 55000, 70000],
    'City': ['New York', 'Freemont', 'Chicago', 'Raleigh', 'New York']
}

df = pd.DataFrame(data)
print(df)
print()

df.to_csv('data_csv0.csv')
df.to_csv('data_csv1.csv',index=False)
df.to_html('data_html.html')

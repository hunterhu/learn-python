#!/bin/python3

#Create a 2D array of shape (3, 4) with random integers between 1 and 10.
#Subtract the mean of each column from each element of the corresponding column.

import numpy as np

arr = np.random.randint(1,10,(3,4))
print(f"given:\n{arr}")

column_means = np.mean(arr, axis=0)
print(f"np.mean of each column:\n{column_means}")

print(f"result:\n{arr - column_means}")

#!/bin/python3

#Create two 1D arrays of the same length with values
#[1, 2, 3, 4, 5] and [2, 3, 4, 5, 6].
#Compute the element-wise sum, difference, product, and division.

import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([2,3,4,5,6])

print(f"given:\n{a} {b}")
print(f"sum:\n{a+b}")
print(f"sub:\n{a-b}")
print(f"mul:\n{a*b}")
print(f"div:\n{a/b}")

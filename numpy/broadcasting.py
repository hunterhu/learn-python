#!/bin/python3

import numpy as np

"""
Array A's shape: (M, N)

Possible shapes of array B:

(1,)
(N,)
(1, N)
(M, 1)
(M, N)

Here's how these possibilities work:

(1,): A 1D array. Broadcasting will stretch it to shape (1, 1) for element-wise operations.

(N,): A 1D array. Broadcasting will stretch it to shape (1, N) for element-wise operations.

(1, N): A 2D array with one row and N columns. Broadcasting will replicate it along the rows to match the M rows of array A.

(M, 1): A 2D array with M rows and one column. Broadcasting will replicate it along the columns to match the N columns of array A.

(M, N): A 2D array with the same shape as array A. Broadcasting can be directly applied as the shapes are already compatible.
"""

print("Rule 1: increase dimension to make compatible")

A = np.array([[1, 2, 3]])
B = np.array([10])
result = A + B
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nResult of A + B:")
print(result)

print("Rule 2: increase dimension size to make compatible")
A = np.array([[1], [2], [3]])
B = np.array([10, 20, 30])
result = A + B
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nResult of A + B:")
print(result)

print("rule 3: incompatible")
# Creating arrays for demonstration
A = np.array([[1, 2, 3]])
B = np.array([10, 20])
try:
    result = A + B
except ValueError as e:
    print("ValueError:", e)

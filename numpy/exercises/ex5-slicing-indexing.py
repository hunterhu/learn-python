#!/bin/python3

#Create a 2D array with values from 1 to 25 and
#reshape it into a (5, 5) array.
#Extract the second column, the third row,
#and a submatrix consisting of the central 3x3 values.

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
                16,17,18,19,20,21,22,23,24,25])
print(f"given:\n{arr}")
arr_2d = np.reshape(arr, (5,5))
print(f"reshape to (5x5)\n{arr_2d}") 

print(f"2nd column:\n{arr_2d[:,1]}")
print(f"3rd row:\n{arr_2d[2,:]}")
print(f"central 3x3 submatrix:\n{arr_2d[1:4,1:4]}")

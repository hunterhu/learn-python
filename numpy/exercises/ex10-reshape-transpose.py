#!/bin/python3

#Create a 1D array with values [1, 2, 3, 4, 5, 6].
#Reshape it into a (2, 3) array and then transpose it.

import numpy as np

arr = np.array([1,2,3,4,5,6])
print(f"given:\n{arr}")
reshaped = np.reshape(arr, (2,3))
print(f"reshape:\n{reshaped}")
transposed = np.transpose(reshaped)
print(f"transpose:\n{transposed}")

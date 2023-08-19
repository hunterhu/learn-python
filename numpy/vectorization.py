#!/bin/python3

import numpy as np

#operations on entire arrays, aka "vectors" WITHOUT LOOPING

print("Element-wise Ops")
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
print(a+b)

print("Broadcasting is also vectorization with different shapes & dimensions")
a = np.array([[1,2],
              [3,4]])
b = np.array([10,20])
print(a+b)

print("Universal Functions, no Looping needed")
arr = np.array([1,2,3,4])
print(np.square(arr))
print(np.sqrt(arr))
print(np.exp(arr))

print("Conditional Ops")
print(np.where(arr > 2, arr, 0))
#!/bin/python3

#Create two 1D arrays with values [1, 2, 3] and [4, 5, 6].
#Concatenate them horizontally and vertically.

import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(f"given:\n{a} {b}")
print(f"hstacked:\n{np.hstack((a,b))}")
print(f"vstacked:\n{np.vstack((a,b))}")

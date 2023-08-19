#!/bin/python3

# Create a 2D array with dimensions (3, 4) containing integers from 1 to 12.
# Reshape it into a (4, 3) array.

import numpy as np

arr_34 = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12]])

print(f"given arr_34:\n{arr_34}")
print(f"reshape to (4,3):\n{np.reshape(arr_34,(4,3))}")
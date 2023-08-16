#!/bin/python3

import numpy as np

arr = np.array([10,20,30,40,50,60])
mask = (arr % 20 == 0)
print(arr[mask])
mask = (arr > 30) & (arr < 50)
print(arr[mask])

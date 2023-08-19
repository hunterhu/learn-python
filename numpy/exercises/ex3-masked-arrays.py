#!/bin/python3

#Create a masked array from a regular array
#with values [5, -999, 10, 15, -999].
#The masked values are -999.
#Calculate the mean of the masked array.

import numpy as np
import numpy.ma as ma

arr = np.array([5, -999, 10, 15, -999])
print(f"given regular array\n{arr}")
masked = ma.masked_where(arr == -999, arr)
print(f"masked arr: {masked}")
print(f"np.mean: {np.mean(masked)}")

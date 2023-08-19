#!/bin/python3

import numpy as np
import numpy.ma as ma  #masked arrays

print(f"Create Masked Arrays: Good for handling missing/invalid values")
data = np.array([1,2,-999,3,4,5])
print(f"Original data: {data}")
my_mask = (data == -999)   #Creating a mask for invalid data

masked_data = ma.array(data, mask=my_mask)
print(f"Masked data: {masked_data}")

print(f"Maskded Arrays allow to perform ops while ignoring masked values")
print(f"Average value: {ma.mean(masked_data)}")

print(f"Use numpy.ma.masked_where() to apply a mask, easier to understand")
print(f"masked data: {ma.masked_where(data == -999, data)}")
print(f"Then the masked values are automatically ignore for operations")
print(f"Add a number to masked_data: {masked_data + 10}")
print(f"We can also filled the masked value with a specific value")
print(f"{masked_data.filled(0)}")
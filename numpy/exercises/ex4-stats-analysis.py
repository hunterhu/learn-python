#!/bin/python3

#Generate a random 1D array of 100 values
#from a normal distribution with mean 0 and standard deviation 1.
#Calculate the mean, standard deviation, and variance of the array.

import numpy as np

data = np.random.rand(100)
print(f"give uniform distribution data:\n{data}")
print(f"np.mean: {np.mean(data)}")
print(f"np.std: {np.std(data)}")
print(f"np.var: {np.var(data)}")

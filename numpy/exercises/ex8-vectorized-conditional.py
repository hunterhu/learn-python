#!/bin/python3

#Generate a random 1D array of 20 integers between 1 and 100.
#Create a new array that contains the squares of even numbers
#and zeros for odd numbers.

import numpy as np

arr = np.random.randint(1,100,20)
print(f"given:\n{arr}")

new= np.where(arr % 2 == 0, arr*arr, 0)
print(f"condition: even-squared, odd-0:\n{new}")

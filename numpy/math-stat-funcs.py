#!/bin/python3

import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])
print(f"given: {a} and {b}")

print(f"np.add: {np.add(a,b)}")
print(f"np.sub: {np.subtract(a,b)}")
print(f"np.mul: {np.multiply(a,b)}")
print(f"np.div: {np.divide(a,b)}")

print("Trignometric Functions")
angle = np.array([0,np.pi/4, np.pi/2])
print(f"given: {angle}")
print(f"np.sin: {np.sin(angle)}")
print(f"np.cos: {np.cos(angle)}")
print(f"np.tan: {np.tan(angle)}")

print(f"Logarithmic & Exponential Functions")
data = np.array([1,2,3])
print(f"given: {data}")
print(f"np.log: {np.log(data)}")
print(f"np.log10: {np.log10(data)}")
print(f"np.exp: {np.exp(data)}")

print(f"Statistical Functions")
data = np.array([1,2,3,4,5,6,7,8,9,10])
print(f"given: {data}")
print(f"np.mean: {np.mean(data)}")
print(f"np.median: {np.median(data)}")
print(f"np.std: {np.std(data)}")
print(f"np.variance: {np.var(data)}")
print(f"np.min: {np.min(data)}")
print(f"np.max: {np.max(data)}")

print(f"Random Number Generator")
random_arr = np.random.rand(5)
print(f"random array: {random_arr}")
random_int = np.random.randint(1,100,size=5)
print(f"random int array: {random_int}")

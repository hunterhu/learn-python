#!/bin/python3

import numpy as np

fname="data.npy"
fzname="data.npz"

print("Saving array as binary file(not readable)")
print("file ext will be and has to be .npy (numpy)")
arr = np.array([1,2,3,4])
np.save(fname, arr)
print(f"loading {fname}")
print(np.load(fname))

print("Saving multiple arrays")
a = np.array([1,2,3])
b = np.array([4,5,6])
np.savez(fzname, arr1=a, arr2=b)
loaded_data = np.load(fzname)
print(f"loaded data from {fzname}")
print(loaded_data["arr1"])
print(loaded_data["arr2"])

print("Saving array as readable text file")
arr_2d = np.array([[1,2,3],
               [4,5,6]])
np.savetxt("data.txt", arr_2d, delimiter=" ")
print(np.loadtxt("data.txt", delimiter=" "))
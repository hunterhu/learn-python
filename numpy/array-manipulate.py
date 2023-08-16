#!/bin/python3

import numpy as np

arr = np.array([1,2,3,4,5,6])
print(arr)
print("Array reshape")
print(arr.reshape(2,3))
print(arr.reshape(3,2))

print("Array flatten")
arr = np.array([[1,2,3],
                [4,5,6]])
print(arr)
print(arr.flatten())

print("Array transpose")
print(arr.transpose())

print("Adding Dimensions: (3,)")
arr = np.array([1,2,3])
print(arr)
print(arr[:, np.newaxis])
print(np.expand_dims(arr, axis=1))

print("Adding Dimensions: (2,2)")
arr = np.array([[1,2],
                [3,4]])
print(arr)
print(arr[:, np.newaxis])
print(arr[:,:, np.newaxis])

print("Removing Dimensions with size 1(only)")
arr = np.array([[1],
                [3]])
print(arr)
print(np.squeeze(arr))

print("Removing Dimensions with (2,2) won't do anything")
arr = np.array([[1,2],
                [3,4]])
print(arr)
print(np.squeeze(arr))

print("Concatenate ...")
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a)
print(b)
print(np.concatenate((a,b)))
print("vstack ...")
print(np.vstack((a,b)))
print("hstack ...")
print(np.hstack((a,b)))

c=np.array([7,8,9])
print(np.vstack((a,b,c)))
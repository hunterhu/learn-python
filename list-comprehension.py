#!/bin/python3

items= [1,2,3,4,5,6]

big = [ (item > 3) for item in items]
print(big)

big = [ item for item in items if item > 3 ]
print(big)

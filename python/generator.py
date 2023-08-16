#!/bin/python3

from sys import getsizeof

values = (x*x/2 for x in range(10))
print(values)
print("values", getsizeof(values))


#object size stays the same no matter the range()
bigvalues = (x*x/2 for x in range(100000))
print(bigvalues)
print("bigvalues", getsizeof(bigvalues))
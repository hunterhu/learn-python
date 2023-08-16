#!/bin/python3

numbers = [1,2,3]

print(numbers)
print(*numbers)

print(list(range(5)))
print(*list(range(5)))

first = [1,2,3]
second= [4,5,6]
print([*first, *second, *"hello"])

#unpacking dictionary
first = {"x":1}
second= {"x":10, "y":20}
combined={**first, **second, "z":30}
print(combined)

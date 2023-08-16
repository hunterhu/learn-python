#!/bin/python3

def test(*list):
    total = 1
    for number in list:
        total *= number
        print(total)
    return total

print(hex(test(1,2,3,4,5,6,7,8,9,10)))


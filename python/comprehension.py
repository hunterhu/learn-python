#!/bin/python3

items= [1,2,3,4,5,6]

big = [ (item > 3) for item in items]
print(big)

big = [ item for item in items if item > 3 ]
print(big)

members = [("hunter", 40), ("Joe", 30), ("Amy", 25)]
young = [ person[0] for person in members if person[1] < 30 ]
print(young)

point = { "x":1, "y":2 }
newpoint = { (key,value*2) for (key,value) in points.items()}
print(newpoint)

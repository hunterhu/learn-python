#!/bin/python3

paragraph = """
    This is a good text for the not too bad example,
    but wait, is this good or bad after all? good
    if you like it, bad if you don't.
"""

words = {"good":0, "bad":0}

print(words["good"])
print(words["bad"])

for word in paragraph.split():
    if word == "good":
        words["good"] += 1
    if word == "bad":
        words["bad"] += 1

print(words["good"])
print(words["bad"])

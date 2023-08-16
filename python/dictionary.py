#!/bin/python3

paragraph = """
    This is a good text for the not too bad example,
    but wait, is this good or bad after all? good
    if you like it, bad if you don't.
"""

words = {}
print(words)

for word in paragraph.split():
    if word not in words:
        words[word] = paragraph.count(word)

print(words)

#!/bin/python3

file_path = "example.txt"

# Writing to a file
new_content = "This is the new content that will be written to the file."
with open(file_path, "w") as file:
    file.write(new_content)
    print("New content written to the file.")

# Reading from a file
with open(file_path, "r") as file:
    content = file.read()
    print("File contents:")
    print(content)

# Appending to a file
append_content = "\nThis is appended content."
with open(file_path, "a") as file:
    file.write(append_content)
    print("Content appended to the file.")

#!/bin/python3

import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="A script to demonstrate multiple required arguments.")

# Add required arguments with short and long option names
parser.add_argument("-n", "--name", type=str, required=True, help="The name of the person")
parser.add_argument("-a", "--age", type=int, required=True, help="The age of the person")

# Parse the command-line arguments
args = parser.parse_args()

# Access the values of the required arguments
name = args.name
age = args.age

print(f"Hello, {name}! You are {age} years old.")

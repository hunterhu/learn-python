#!/bin/python3

import numpy as np

print(f"Creating structure array")
data = np.array([(1, "Alice", 25),
                 (2, "Bob", 30),
                 (3, "Charlie", 28)],
                dtype=[("id", int),
                       ("name", "U10"),
                       ("age", int)])

print(data)

print(f"Access certain data type")
print(data["name"])

print(f"Access with conditional filter")
print(data[data["age"] > 26])

print(f"Modify certain data field")
data["age"] += 1
print(data)

print(f"Nested structured arrays")
data = np.array([(1, ("Alice", "Johnson"), 25),
                 (2, ("Bob", "Smith"), 26)],
                dtype=[("id", int),
                       ("name", [("first", "U10"), ("last", "U10")]),
                       ("age", int)])
print(data)

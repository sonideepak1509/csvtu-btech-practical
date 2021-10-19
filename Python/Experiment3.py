# Write programs to understand the use of Numpy’s Ndarray, Basic Operations, Indexing, Slicing,
# and Iterating, Conditions and Boolean Arrays.

# Numpy's Ndarray

import numpy as np

# One Dimension

a = np.array([1, 3, 5])
print(a)

# Two Dimensions

b = np.array([[1, 3], [2, 4]])
print(b)

# Minimum Dimension

c = np.array([1, 2, 3, 4, 5], ndmin=2)
print(c)

# dtype parameter

d = np.array([1, 2, 3], dtype=complex)
print(d)

# Basic Operations
# Indexing
# One dimension

print(a[0])

print(a[1])

# Two Dimensions

print("2nd element of first row", b[0, 1])

# Slicing
# one Dimension

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])

print(arr[4:])

print(arr[:4])

# Negative Slicing

print(arr[-3:-1])

# Step

print(arr[1:5:2])

# Two Dimensions

arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr2[1, 1:4])

print(arr2[0:2, 2])

print(arr2[0:2, 1:4])

# Iterating
# One Dimension

for x in a:
    print(x)

# Two Dimensions

for y in b:
    print(y)

# Iterate on each scalar element of the 2-D array:

for x in b:
    for y in x:
        print(y)

# Iterating Arrays Using nditer()

for x in np.nditer(b):
    print(x)

# Boolean array

d = np.reshape(np.arange(16), (4, 4))
# create a 4x4 array of integers
print(d)

large_values = (d > 10) # test which elements of a are greated than 10
print(large_values)

# Write programs to understand the use of Numpy’s Shape Manipulation, Array Manipulation, Vectorization.

# Shape Manipulation

import numpy as np

a = np.random.random((8))
print(a)

# convert a 1-D NumPy array into a matrix or 2-D  NumPy array

A = a.reshape(2, 4)
print(A)

# convert 2-D arrays into one-dimensional arrays

A = A.ravel()
print(A)

# Array Manipulation

b = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])

# Transpose

print(np.transpose(b))
# Or
print(b.T)

# Joining Array

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

print(np.concatenate((x, y)))


# vectorization of Array

# Dot product
import time
import numpy
import array

# 8 bytes size int
X = array.array('q')
for i in range(100000):
	X.append(i);

Y = array.array('q')
for i in range(100000, 200000):
	Y.append(i)

# classic dot product of vectors implementation
tic = time.process_time()
dot = 0.0;

for i in range(len(X)):
	dot += X[i] * Y[i]

toc = time.process_time()

print("dot_product = "+ str(dot));
print("Computation time = " + str(1000*(toc - tic )) + "ms")


n_tic = time.process_time()
n_dot_product = numpy.dot(X, Y)
n_toc = time.process_time()

print("\nn_dot_product = "+str(n_dot_product))
print("Computation time = "+str(1000*(n_toc - n_tic ))+"ms")

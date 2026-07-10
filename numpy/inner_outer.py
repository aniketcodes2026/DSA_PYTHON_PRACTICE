# Problem: Inner and Outer
# Platform: HackerRank
# Concept: NumPy / Inner Product / Outer Product


import numpy

a = numpy.array(input().split(), int) # List comprehension to read a line of input and create a 1D array of integers
b = numpy.array(input().split(), int) # The above line does the same for the second array

print(numpy.inner(a, b)) # The numpy.inner() function computes the inner product of two arrays. For 1-D arrays, it is equivalent to the dot product of the vectors. For higher-dimensional arrays, it sums the products of the elements over the last axis of the first array and the second-to-last axis of the second array.
print(numpy.outer(a,b)) # The numpy.outer() function computes the outer product of two vectors. For 1-D arrays, it returns the matrix product of the first array and the transpose of the second array. For higher-dimensional arrays, it returns the product of the first array and the second array, where the first array is treated as a column vector and the second array is treated as a row vector.

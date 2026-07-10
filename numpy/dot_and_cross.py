# Problem: Dot and Cross
# Platform: HackerRank
# Concept: NumPy / Matrix Multiplication

import numpy

n = int(input())

a = numpy.array([input().split() for _ in range(n)], int) # List comprehension to read n lines of input and create a 2D array (matrix) of integers
b = numpy.array([input().split() for _ in range(n)], int) # The above line does the same for the second matrix


print(numpy.dot(a, b)) # The numpy.dot() function computes the dot product of two arrays. For 2-D arrays, it is equivalent to matrix multiplication.

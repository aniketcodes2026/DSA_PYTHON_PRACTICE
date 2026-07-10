# Problem: Linear Algebra
# Platform: HackerRank
# Concept: NumPy / Linear Algebra

import numpy

n=int(input())
array=numpy.array([input().split() for _ in range(n)],float) # List comprehension to read n lines of input and create a 2D array (matrix) of floats
print(round(numpy.linalg.det(array),2)) #The linalg.det tool computes the determinant of an array. #round off to 2 decimal places
 
vals,vecs = numpy.linalg.eig(array)  #The linalg.eig tool computes the eigenvalues and right eigenvectors of a square array.
print(vals) #The eigenvalues are returned in a 1D array, and the corresponding right eigenvectors are returned in a 2D array, where the i-th column is the eigenvector corresponding to the i-th eigenvalue.
print(vecs) #The eigenvalues are returned in a 1D array, and the corresponding right eigenvectors are returned in a 2D array, where the i-th column is the eigenvector corresponding to the i-th eigenvalue.

print(numpy.linalg.inv(array))  #The linalg.inv tool computes the (multiplicative) inverse of a matrix.

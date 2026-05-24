# Problem: Linear Algebra
# Platform: HackerRank
# Concept: NumPy / Linear Algebra

import numpy
n=int(input())
array=numpy.array([input().split() for _ in range(n)],float)
print(round(numpy.linalg.det(array),2)) #The linalg.det tool computes the determinant of an array. #round off to 2 decimal places
 
vals,vecs = numpy.linalg.eig(array)  #The linalg.eig tool computes the eigenvalues and right eigenvectors of a square array.
print(vals)
print(vecs)

print(numpy.linalg.inv(array))  #The linalg.inv tool computes the (multiplicative) inverse of a matrix.

# Problem: Dot and Cross
# Platform: HackerRank
# Concept: NumPy / Matrix Multiplication

import numpy

n = int(input())

a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)

print(numpy.dot(a, b))
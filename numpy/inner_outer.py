# Problem: Inner and Outer
# Platform: HackerRank
# Concept: NumPy / Inner Product / Outer Product

import numpy

a = numpy.array(input().split(), int)
b = numpy.array(input().split(), int)

print(numpy.inner(a, b))
print(numpy.outer(a,b))

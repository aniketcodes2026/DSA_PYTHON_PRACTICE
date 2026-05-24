# Problem: Polynomials
# Platform: HackerRank
# Concept: NumPy / Polynomial Evaluation

import numpy

poly=list(map(float,input().split()))
x=float(input())
print(numpy.polyval(poly,x))  #The polyval tool evaluates the polynomial at specific value.

print(numpy.roots(poly))  #The roots tool returns the roots of a polynomial with the given coefficients.

print(numpy.poly(poly))   #The poly tool returns the coefficients of a polynomial with the given sequence of roots.

print(numpy.polyint(poly))  #The polyint tool returns an antiderivative (indefinite integral) of a polynomial.

print(numpy.polyder(poly))  #The polyder tool returns the derivative of the specified order of a polynomial.

print(numpy.polyfit(poly))  #The polyfit tool fits a polynomial of a specified order to a set of data using a least-squares approach.

#The functions polyadd, polysub, polymul, and polydiv also handle proper addition, subtraction, multiplication, and division of polynomial coefficients, respectively.
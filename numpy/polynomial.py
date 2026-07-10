# Problem: Polynomials
# Platform: HackerRank
# Concept: NumPy / Polynomial Evaluation

import numpy


poly=list(map(float,input().split())) # List comprehension to read a line of input, split it into components, convert each component to a float, and create a list of these floats representing the coefficients of the polynomial. The coefficients are typically ordered from the highest degree to the lowest degree (i.e., poly[0] is the coefficient of x^n, poly[1] is the coefficient of x^(n-1), and so on).

x=float(input()) # The above line reads a single line of input, converts it to a float, and assigns it to the variable x. This value will be used as the point at which to evaluate the polynomial defined by the coefficients in the poly list.

print(numpy.polyval(poly,x))  #The polyval tool evaluates the polynomial at specific value.

print(numpy.roots(poly))  #The roots tool returns the roots of a polynomial with the given coefficients.

print(numpy.poly(poly))   #The poly tool returns the coefficients of a polynomial with the given sequence of roots.

print(numpy.polyint(poly))  #The polyint tool returns an antiderivative (indefinite integral) of a polynomial.

print(numpy.polyder(poly))  #The polyder tool returns the derivative of the specified order of a polynomial.

print(numpy.polyfit(poly))  #The polyfit tool fits a polynomial of a specified order to a set of data using a least-squares approach.

#The functions polyadd, polysub, polymul, and polydiv also handle proper addition, subtraction, multiplication, and division of polynomial coefficients, respectively.

#Problem: itertools.product()
# Platform: HackerRank
# Concept: Itertools / Cartesian Product


from itertools import product

A = list(map(int, input().split())) # Read the first list of integers
B = list(map(int, input().split())) # Read the second list of integers

print(*product(A, B)) # Print the Cartesian product of lists A and B

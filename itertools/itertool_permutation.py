# Problem: itertools.permutations()
# Platform: HackerRank
# Concept: Itertools / Permutations

from itertools import permutations

s, k = input().split() # Read the string and the permutation size

for p in permutations(sorted(s), int(k)): # Generate all permutations of the sorted string s of length k
    print(''.join(p)) # Print each permutation as a string

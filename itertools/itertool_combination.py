# Problem: itertools.combinations()
# Platform: HackerRank
# Concept: Itertools / Combinations

from itertools import combinations

s, k = input().split() # Read the string and the maximum combination size

for i in range(1, int(k) + 1): # Loop through all combination sizes from 1 to k
    for c in combinations(sorted(s), i): # Generate all combinations of the sorted string s of length i
        
        print(''.join(c)) #prints all the combinations of the characters in the string s with length from 1 to k, sorted in lexicographic order

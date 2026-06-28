# Problem: No Idea!
# Platform: HackerRank
# Concept: Sets
# Description: Calculate the happiness score based on whether array elements belong to set A (+1) or set B (-1).

n, m = map(int, input().split())

arr = list(map(int, input().split())) # Read the array of integers

A = set(map(int, input().split())) # Read the set A
B = set(map(int, input().split())) # Read the set B

happiness = 0

for num in arr:
    if num in A:
        happiness += 1
    elif num in B:
        happiness -= 1

print(happiness)

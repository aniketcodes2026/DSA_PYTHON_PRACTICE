# Problem: No Idea!
# Platform: HackerRank
# Concept: Sets

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
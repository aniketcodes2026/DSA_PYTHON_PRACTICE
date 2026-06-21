# Problem: Set .add()
# Platform: HackerRank
# Concept: Sets

countries = set()

for _ in range(int(input())): 
    countries.add(input()) # add() method adds an element to the set if it is not already present. If the element is already present, the set remains unchanged.

print(len(countries))
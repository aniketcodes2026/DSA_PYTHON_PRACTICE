# Problem: Introduction to Sets
# Platform: HackerRank
# Concept: Sets

n = int(input())
array = list(map(int, input().split()))

def average(array):
    distinct_heights = set(array)
    return sum(distinct_heights) / len(distinct_heights)

result = average(array)
print(result)

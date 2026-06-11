# Problem: Find the Runner-Up Score
# Platform: HackerRank
# Concept: Lists / Sorting

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
largest=arr[-1]
while arr[-1]==largest:
    arr.pop()
print(arr[-1])
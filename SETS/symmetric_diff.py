# Problem: Symmetric Difference
# Platform: HackerRank
# Concept: Sets

m = int(input())
A = set(map(int, input().split()))

n = int(input())
B = set(map(int, input().split()))

result = A.symmetric_difference(B)

for num in sorted(result):
    print(num)
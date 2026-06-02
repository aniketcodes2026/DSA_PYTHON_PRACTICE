# Problem: collections.Counter()
# Platform: HackerRank
# Concept: Collections / Counter

from collections import Counter

n = int(input())
shoes = list(map(int, input().split()))

counter = Counter(shoes)

money = 0

for _ in range(int(input())):
    size, price = map(int, input().split())

    if counter[size] > 0:
        money += price
        counter[size] -= 1

print(money)
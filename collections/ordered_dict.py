# Problem: collections.OrderedDict()
# Platform: HackerRank
# Concept: Collections / OrderedDict

from collections import OrderedDict

n = int(input())

items = OrderedDict()

for _ in range(n):
    item = input().split()
    
    name = " ".join(item[:-1])
    price = int(item[-1])

    items[name] = items.get(name, 0) + price

for name, total in items.items():
    print(name, total)
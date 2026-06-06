# Problem: Collections.OrderedDict()
# Platform: HackerRank
# Concept: Collections / OrderedDict


from collections import OrderedDict

n = int(input())

items = OrderedDict()

for _ in range(n):
    entry = input().split()

    item_name = " ".join(entry[:-1])
    price = int(entry[-1])

    if item_name in items:
        items[item_name] += price
    else:
        items[item_name] = price

for item, total in items.items():
    print(item, total)
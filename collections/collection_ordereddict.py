# Problem: Collections.OrderedDict()
# Platform: HackerRank
# Concept: Collections / OrderedDict

from collections import OrderedDict

n = int(input())
items = OrderedDict()

for _ in range(n):
    entry = input().split() # split the input line into words, the last word is the price, the rest is the item name

    item_name = " ".join(entry[:-1]) # join all the words except the last one to get the item name, since the item name can have spaces in it
    price = int(entry[-1])

    if item_name in items:
        items[item_name] += price 
    else:
        items[item_name] = price

for item, total in items.items():
    print(item, total) # print the item name and the total price for that item, in the order they were first added to the dictionary

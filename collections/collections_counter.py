# Problem: collections.Counter()
# Platform: HackerRank
# Concept: Collections / Counter

from collections import Counter

n = int(input())
shoes = list(map(int, input().split())) # read the number of shoes and the sizes of the shoes available in the store, and store them in a list called shoes

counter = Counter(shoes)

money = 0

for _ in range(int(input())):
    size, price = map(int, input().split()) # read the size and price of the shoe being sold

    if counter[size] > 0:
        money += price
        counter[size] -= 1

print(money) # print the total money earned from selling the shoes
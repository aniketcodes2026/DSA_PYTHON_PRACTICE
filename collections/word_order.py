# Problem: Word Order
# Platform: HackerRank
# Concept: Collections / OrderedDict

from collections import OrderedDict

n = int(input())

words = OrderedDict()

for _ in range(n):
    word = input()

    if word in words:
        words[word] += 1
    else:
        words[word] = 1

print(len(words))
print(*words.values())
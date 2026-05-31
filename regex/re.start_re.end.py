# Problem: Re.start() & Re.end()
# Platform: HackerRank
# Concept: Regular Expressions (Regex)


import re

S = input()
k = input()

matches = list(re.finditer(f'(?={k})', S))

if matches:
    for match in matches:
        start = match.start()
        end = start + len(k) - 1
        print((start, end))
else:
    print((-1, -1))
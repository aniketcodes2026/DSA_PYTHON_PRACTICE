# Problem: Re.start() & Re.end()
# Platform: HackerRank
# Concept: Regular Expressions (Regex)


import re

S = input()
k = input()

matches = list(re.finditer(f'(?={k})', S)) # Find all overlapping matches of the substring k in the string S

if matches:
    for match in matches:
        start = match.start() # Get the starting index of the match
        end = start + len(k) - 1 # Get the ending index of the match
        print((start, end))
else:
    print((-1, -1))
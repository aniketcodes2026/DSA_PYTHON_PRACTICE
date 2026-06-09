# Problem: Triangle Quest 2
# Platform: HackerRank
# Concept: Pattern Printing
# Condition: should be in less than 3 lines of code

for i in range(1, int(input()) + 1):
    print(((10**i - 1) // 9) ** 2)
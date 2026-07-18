# Problem: Triangle Quest 2
# Condition: should be in less than 3 lines of code
# Platform: HackerRank
# Concept: Pattern Printing


for i in range(1, int(input()) + 1):
    print(((10**i - 1) // 9) ** 2)

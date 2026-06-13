# Problem: Designer Door Mat
# Platform: HackerRank
# Concept: Strings / Pattern Printing


n, m = map(int, input().split())
for i in range(n // 2):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(m, "-")) #print pattern in the middle
print("WELCOME".center(m, "-")) #print welcome in the middle

for i in range(n // 2 - 1, -1, -1):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(m, "-")) #print pattern in the middle
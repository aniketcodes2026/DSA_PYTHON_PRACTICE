# Problem: Alphabet Rangoli
# Platform: HackerRank
# Concept: Strings / Pattern Printing

def print_rangoli(size):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    width = 4 * size - 3

    for i in range(size - 1, -1, -1):
        s = "-".join(alpha[i:size])
        row = s[::-1] + s[1:]
        print(row.center(width, "-"))

    for i in range(1, size):
        s = "-".join(alpha[i:size])
        row = s[::-1] + s[1:]
        print(row.center(width, "-"))

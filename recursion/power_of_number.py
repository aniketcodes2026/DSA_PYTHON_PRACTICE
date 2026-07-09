# Problem: Power of a Number
# Concept: Recursion
# Platform: HackerRank

def power(a, b):
    if b == 0:
        return 1

    return a * power(a, b - 1) # Recursion: a^b = a * a^(b-1)
#EXAMPLE:
print(power(2, 5))

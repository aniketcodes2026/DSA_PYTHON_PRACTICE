# Problem: Sum of Natural Numbers
# Concept: Recursion

def natural_sum(n):
    if n == 1:
        return 1

    return n + natural_sum(n - 1)

print(natural_sum(5))
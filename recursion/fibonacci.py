# Problem: Fibonacci Using Recursion
# Concept: Recursion
# platform: HackerRank
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. The task is to find the Fibonacci number at a given position using recursion.

def fibonacci(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2) # F(n) = F(n-1) + F(n-2)

num = int(input("Enter position: "))
print("Fibonacci number =", fibonacci(num)) # prints the Fibonacci number at the input position

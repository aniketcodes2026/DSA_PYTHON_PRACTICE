# Problem: Factorial Using Recursion
# Concept: Recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1) # n! = n * (n-1)!

num = int(input("Enter a number: "))
print("Factorial =", factorial(num)) # prints the factorial of the input number

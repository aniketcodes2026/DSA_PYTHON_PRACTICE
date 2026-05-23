# Problem: Fibonacci Using Recursion
# Concept: Recursion

def fibonacci(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("Enter position: "))
print("Fibonacci number =", fibonacci(num))
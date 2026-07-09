# Problem: Print Numbers from 1 to N
# Concept: Recursion

def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1) #prints 1 to n-1
    print(n) #prints n after printing 1 to n-1

#EXAMPLE:
print_1_to_n(5) 

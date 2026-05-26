# Problem: Check Palindrome Using Slicing
# Concept: String Slicing

s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
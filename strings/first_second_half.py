# Problem: Print First and Second Half
# Concept: String Slicing

s = input("Enter a string: ")

mid = len(s) // 2

print("First Half:", s[:mid])
print("Second Half:", s[mid:])
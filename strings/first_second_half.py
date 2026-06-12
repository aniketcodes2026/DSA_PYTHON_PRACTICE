# Problem: Print First and Second Half
# Concept: String Slicing

s = input("Enter a string: ")

mid = len(s) // 2

print("First Half:", s[:mid]) #print characters from the start to the middle index (exclusive)
print("Second Half:", s[mid:]) #print characters from the middle index to the end of the string
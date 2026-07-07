# Problem: Rotate String
# Concept: String Slicing
# Platform: hackerRank

s = input("Enter a string: ")

rotated = s[1:] + s[0]
print(rotated) # print the rotated string by slicing the first character and concatenating it to the end of the string

# Problem: Reverse String Using Recursion
# Concept: Recursion / Strings
# Platform: HackerRank

def reverse_string(s):
    if len(s) == 0:
        return s

    return reverse_string(s[1:]) + s[0] # Recursion: reverse(s) = reverse(s[1:]) + s[0]

print(reverse_string("hello"))
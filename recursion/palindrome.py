# Problem: Check Palindrome Using Recursion
# Concept: Recursion / Strings
# platform: HackerRank
# A palindrome is a word, phrase, number, or other sequence of characters that reads the

def palindrome(s):
    if len(s) <= 1:
        return True # A string of length 0 or 1 is a palindrome

    if s[0] != s[-1]:
        return False # If the first and last characters are different, it's not a palindrome
 
    return palindrome(s[1:-1]) # checks if the first and last characters are the same, then recursively checks the substring excluding the first and last characters

print(palindrome("madam"))
# Problem: Capitalize!
# Platform: HackerRank
# Concept: Strings

def capital(s):
    return ' '.join(word.capitalize() for word in s.split(' ')) #makes the first letter of the word capital
#EXAMPLE:
print(capital("aniket"))

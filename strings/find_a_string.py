# Problem: Find a String
# Platform: HackerRank
# Concept: Strings / Substrings

def count_substring(string, sub_string):
    count = 0

    for i in range(len(string)):
        if string[i:].startswith(sub_string): #startswith() method returns True if the string starts with the specified prefix, otherwise False
            count += 1

    return count

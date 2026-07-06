# Problem: Mutations
# Platform: HackerRank
# Concept: Strings

def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

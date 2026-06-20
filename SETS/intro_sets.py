# Problem: Introduction to Sets
# Platform: HackerRank
# Concept: Sets

def average(array):
    distinct_heights = set(array) # Create a set to store distinct heights
    return sum(distinct_heights) / len(distinct_heights) # Calculate the average of distinct heights
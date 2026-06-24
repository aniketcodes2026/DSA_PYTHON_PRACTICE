# Problem: Symmetric Difference
# Platform: HackerRank
# Concept: Sets

m = int(input())
A = set(map(int, input().split())) # map() function applies a given function to each item of an iterable (like a list) and returns a list of the results. In this case, it converts each input string into an integer before creating the set A.

n = int(input())
B = set(map(int, input().split())) # Similarly, this line creates set B from the input integers.

result = A.symmetric_difference(B) # The symmetric_difference() method returns a set that contains all items from both sets, except items that are present in both sets. In other words, it returns the elements that are in either set A or set B but not in both.

for num in sorted(result): # Sort the result and print each element
    print(num)
# Problem: Palindrome Number
# Platform: LeetCode
# Concept: Number Manipulation


class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        div = 1
        while x>=10*div:
            div*=10
        while div>1:
            left=x/div
            right=x%10
            if left != right:
                return False
# Problem: Two Sum
# Platform: LeetCode
# Concept: Arrays / Hash Maps

class Solution(object):
    
    def twoSum(self, nums, target): 
        for i in range(len(nums)): #\
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]

print(Solution().twoSum([2,7,11,15],9)) #EXAMPLE: The function is called with the input list [2,7,11,15] and the target value 9. It returns the indices of the two numbers that add up to 9, which are 0 and 1 (corresponding to the numbers 2 and 7).

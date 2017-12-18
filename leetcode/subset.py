# Lintcode 17. Subsets 

#version 1: Bit operation:
class Solution:
    
    """
    @param: nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return [[]]
        n = len(nums)
        res = []
        i = 0
        nums.sort()
        while i < (1 << n):
            temp = []
            for j in range(n):
                if (i >> j) & 1 == 1:
                    temp.append(nums[j])
            res.append(temp[:])
            i += 1
        return res

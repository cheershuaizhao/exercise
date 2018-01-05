'''

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
'''

class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0
            
        for i in range(len(nums) - 1, -1, -1):
            if i != len(nums) - 1 and i != len(nums) - 2 and \
            nums[i] == nums[i + 1] and nums[i] == nums[i + 2]:
                del nums[i]
        return len(nums)

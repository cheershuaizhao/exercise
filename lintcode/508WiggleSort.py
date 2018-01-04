'''
Given an unsorted array nums, reorder it in-place such that

nums[0] <= nums[1] >= nums[2] <= nums[3]....

'''












class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    def wiggleSort(self, nums):
    # Write your code here
        n = len(nums)
        for i in xrange(1, n):
            if i % 2 == 1 and nums[i] < nums[i - 1] or \
                i % 2 == 0 and nums[i] > nums[i - 1]:
                nums[i], nums[i - 1] = nums[i- 1], nums[i]
#version 2: sort + replace    
    def wiggleSort(self, nums):
        # write your code here
        # if nums is None or len(nums) == 0:
        #     return
        # self.quicksort(nums, 0, len(nums) - 1)
        nums.sort()
        i = 2
        while i < len(nums):
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
            i += 2
            
#version 3 : quicksort + replace 

    def wiggleSort(self, nums):
        write your code here
        if nums is None or len(nums) == 0:
            return
        self.quicksort(nums, 0, len(nums) - 1)
        # nums.sort()
        for i in range(len(nums)):
            if i % 3 == 2:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
    def quicksort(self, nums, p, r):
        if p < r:
            q = self.partition(nums, p, r)
            self.quicksort(nums, p, q - 1)
            self.quicksort(nums, q + 1, r)
    
    def partition(self, nums, p, r):
        i = p -1
        pivot = nums[r]
        for j in range(p, r - 1):
            if nums[j] <= pivot:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

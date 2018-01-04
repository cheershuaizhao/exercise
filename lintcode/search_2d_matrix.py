

Write an efficient algorithm that searches for a value in an m x n matrix, return the occurrence of it.

This matrix has the following properties:

    Integers in each row are sorted from left to right.
    Integers in each column are sorted from up to bottom.
    No duplicate integers in each row or column.



class Solution:
    """
    @param: matrix: A list of lists of integers
    @param: target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix is None or len(matrix) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        cnt = 0
        for i in range(m):
            if matrix[i][0] > target:
                break
            if self.search(matrix[i], target):
                cnt += 1
        return cnt
        
        
        
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            if nums[mid] < target:
                start = mid
            if nums[mid] > target:
                end = mid
        if nums[start] == target or nums[end] == target:
            return True
        return False

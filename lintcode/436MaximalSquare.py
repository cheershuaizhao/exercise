'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.
'''

'''
Think about CNN method
'''

class Solution:
    """
    @param: matrix: a matrix of 0 and 1
    @return: an integer
    """
    def maxSquare(self, matrix):
        # write your code here
        if matrix is None or len(matrix) == 0:
            return 0
            
        m = len(matrix)
        n = len(matrix[0])
        k = min(m, n)
        res = 0
        
        for i in range(1, k + 1):
            if self.searchGood(matrix, i):
                res = i
            else:
                break
        return res ** 2
            
            
    def searchGood(self, matrix, i):
        m = len(matrix)
        n = len(matrix[0])
        for sx in range(m - i + 1):
            for sy in range(n - i + 1):
                if self.isGood(matrix, sx, sy, i):
                    return True
        return False
    
    def isGood(self, matrix, sx, sy, k):
        for i in range(sx, sx + k):
            for j in range(sy, sy + k):
                if matrix[i][j] != 1:
                    return False
        return True

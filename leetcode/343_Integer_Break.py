'''343. Integer Break
 Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58. 
'''


'''
Count how many 3 and 2 are in n. The corner cases are when n == 2 or n == 3.
'''


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        if n % 3 == 0:
            res = 3 ** (n // 3)
        if n % 3 == 2:
            res = (3 ** (n // 3)) * 2
        if n % 3 == 1:
            res = (3 ** (n // 3 - 1)) * 4
        return res

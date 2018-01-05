'''
Given two binary strings, return their sum (also a binary string).
'''

class Solution:
    """
    @param: a: a number
    @param: b: a number
    @return: the result
    """
    def addBinary(self, a, b):
        # write your code here
        na = self.helper(a)
        nb = self.helper(b)
        ab = na + nb
        res = []
        if ab == 0:
            return "0"
        while ab != 0:
            res.append(str(ab % 2))
            ab //= 2
        res.reverse()
        res = "".join(res)
        return res
        
    
    def helper(self, s):
        res = 0
        for i in range(len(s)):
            res += int(s[i]) * (2 ** (len(s) - 1 - i))
        return res

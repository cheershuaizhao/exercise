#463. Sort Integers


class Solution:
    """
    @param: A: an integer array
    @return: 
    """
    def sortIntegers(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return
        B = self.mergesort(A)
        A[:] = B[:]
        return
    
    def mergesort(self, A):
        if len(A) <= 1:
            return A
        left = self.mergesort(A[: len(A) // 2])
        right = self.mergesort(A[len(A) // 2: ])
        res = self.comb(left, right)
        return res
        
    def comb(self, left, right):
        i = 0
        j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res.extend(left[i:])
        res.extend(right[j:])
        return res

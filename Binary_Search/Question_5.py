""" 
5. Guess Number Higher or Lower
"""
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        
        while left <= right:
            middle = left + (right - left) // 2
            result = guess(middle)
            if result == 0:
                return middle
            elif result == -1:
                right = middle - 1
            else:
                left = middle + 1
        
        return -1
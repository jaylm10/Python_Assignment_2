"""
18. Arranging Coins
"""

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            if mid * (mid + 1) // 2 == n:
                return mid
            elif mid * (mid + 1) // 

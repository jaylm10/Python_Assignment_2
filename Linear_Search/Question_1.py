"""
1. Find the Maximum Number in a List
"""

class Solution(object):
    def findMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        max_num = nums[0]
        for num in nums:
            if num > max_num:
                max_num = num
        return max_num

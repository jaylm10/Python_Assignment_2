"""
2. Find the Minimum Number in a List
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        min_num = nums[0]
        for num in nums:
            if num < min_num:
                min_num = num
        return min_num

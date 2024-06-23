"""
16. Split Array Largest Sum
"""

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def can_split(nums, m, max_sum):
            current_sum, splits = 0, 1
            for num in nums:
                if current_sum + num > max_sum:
                    current_sum = num
                    splits += 1
                    if splits > m:
                        return False
                else:
                    current_sum += num
            return True
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if can_split(nums, m, mid):
                right = mid
            else:
                left = mid + 1
        return left

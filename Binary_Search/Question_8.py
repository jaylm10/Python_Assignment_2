"""
8. Find First and Last Position in Sorted Array
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary_search_left(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        def binary_search_right(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left

        left, right = binary_search_left(nums, target), binary_search_right(nums, target) - 1
        if left <= right:
            return [left, right] if right < len(nums) and nums[left] == target and nums[right] == target else [-1, -1]
        return [-1, -1]

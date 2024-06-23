"""
15. Find Rotation Count in Sorted Array
"""

class Solution(object):
    def findRotationCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] <= nums[right]:
                return left
            mid = (left + right) // 2
            next = (mid + 1) % len(nums)
            prev = (mid - 1 + len(nums)) % len(nums)
            if nums[mid] <= nums[next] and nums[mid] <= nums[prev]:
                return mid
            elif nums[mid] <= nums[right]:
                right = mid - 1
            elif nums[mid] >= nums[left]:
                left = mid + 1
        return 0

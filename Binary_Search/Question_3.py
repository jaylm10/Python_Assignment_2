"""
3. Binary Search to find the floor and ceil of an element in an array
"""
class Solution(object):
    def findFloorAndCeil(self, nums, target):

        n = len(nums)
        if n == 0:
            return None, None
        
        floor, ceil = -1, -1
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return nums[mid], nums[mid]
            elif nums[mid] < target:
                floor = nums[mid]
                left = mid + 1
            else:
                ceil = nums[mid]
                right = mid - 1
        
        return floor, ceil

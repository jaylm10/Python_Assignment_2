"""
13. Find in Mountain Array
"""

class Solution(object):
    def findInMountainArray(self, target, mountainArr):
        """
        :type target: int
        :type mountainArr: List[int]
        :rtype: int
        """
        def binary_search(arr, target, left, right, key=lambda x: x):
            while left <= right:
                mid = (left + right) // 2
                if key(arr[mid]) == target:
                    return mid
                elif key(arr[mid]) < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        peak = self.peakIndexInMountainArray(mountainArr)
        left_res = binary_search(mountainArr, target, 0, peak)
        if left_res != -1:
            return left_res
        return binary_search(mountainArr, target, peak + 1, len(mountainArr) - 1, key=lambda x: -x)

    def peakIndexInMountainArray(self, arr):
        left, right = 0, len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left

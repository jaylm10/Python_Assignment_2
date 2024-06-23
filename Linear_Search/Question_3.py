"""
3. Find if a Character k is Present in a String
"""

class Solution(object):
    def isCharPresent(self, s, k):
        """
        :type s: str
        :type k: str
        :rtype: bool
        """
        for char in s:
            if char == k:
                return True
        return False

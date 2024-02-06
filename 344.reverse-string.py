#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                reverse(l + 1, r - 1)
        reverse(0, len(s) - 1)
# @lc code=end


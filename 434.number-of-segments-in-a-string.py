#
# @lc app=leetcode id=434 lang=python3
#
# [434] Number of Segments in a String
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if (i == 0 or s[i-1]==" ") and s[i] !=" ":
                count += 1
        return count
# @lc code=end


#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ds = (s + s)[1:-1]
        print(ds)
        return s in ds
# @lc code=end


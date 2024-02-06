#
# @lc app=leetcode id=709 lang=python3
#
# [709] To Lower Case
#

# @lc code=start
class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        for c in s:
            n = ord (c)
            if n > 64 and n < 91:
                ans += chr(n + 32)
            else:
                ans += c
        return ans


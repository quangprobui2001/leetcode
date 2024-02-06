#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        if n & n - 1 != 0:
            return False
        b = bin(n)[::-1]
        p = b.index("1")
        return p % 2 == 0
# @lc code=end


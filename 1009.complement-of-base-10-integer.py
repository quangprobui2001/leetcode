#
# @lc app=leetcode id=1009 lang=python3
#
# [1009] Complement of Base 10 Integer
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0: 
            return 1 
        x = 1 
        while x <= N: x <<= 1 
        return (x - 1) ^ N
# @lc code=end


#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_value = x ^ y
        count = 0
        while x_value != 0:
            count += 1
            x_value &= (x_value - 1)
        return count

# @lc code=end


#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l , output = 0, 0
        for r, n in enumerate(nums):
            if n == 0:
                l = r + 1
            output = max(output, r - l + 1)
        return output 
# @lc code=end


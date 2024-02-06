#
# @lc app=leetcode id=645 lang=python
#
# [645] Set Mismatch
#

# @lc code=start
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        duplication = sum(nums) - sum(set(nums))
        missing = n * (n + 1) // 2 - sum(set(nums))
        return [duplication, missing]
        
# @lc code=end


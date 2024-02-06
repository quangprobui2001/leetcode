#
# @lc app=leetcode id=961 lang=python3
#
# [961] N-Repeated Element in Size 2N Array
#

# @lc code=start
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        unique = set()
        for num in nums:
            if num not in unique:
                unique.add(num)
            else:
                return num
# @lc code=end


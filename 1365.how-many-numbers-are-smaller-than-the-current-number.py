#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        info = {}
        for i, num in enumerate(sorted(nums)):
            if num not in info:
                info[num] = i
        return [info[num] for num in nums]
# @lc code=end


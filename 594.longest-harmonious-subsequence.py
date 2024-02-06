#
# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#

# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = 0
        for x in c:
            if x + 1 in c:
                res = max(res, c[x] + c[x + 1])
        return res
# @lc code=end


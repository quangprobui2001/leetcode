#
# @lc app=leetcode id=575 lang=python3
#
# [575] Distribute Candies
#

# @lc code=start
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        total = len(candyType)
        max = total // 2
        candies = set(candyType)
        diff = len(candies)
        if diff > max:
            return max
        else: 
            return diff
        return min(len(candies)//2, len(set(candyType)))
# @lc code=end


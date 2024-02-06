#
# @lc app=leetcode id=1128 lang=python3
#
# [1128] Number of Equivalent Domino Pairs
#

# @lc code=start
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pair = {}
        count = 0
        for domino in dominoes:
            key = tuple(sorted(domino))
            count += pair.setdefault(key, 0)
            pair[key] += 1
        return count
# @lc code=end


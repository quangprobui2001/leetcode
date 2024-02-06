#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sc = sorted(score, reverse=True)
        count = {}
        for i in range(len(sc)):
            if i == 0:
                count[sc[i]] = "Gold Medal"
            elif i == 1:
                count[sc[i]] = "Silver Medal"
            elif i == 2:
                count[sc[i]] = "Bronze Medal"
            else:
                count[sc[i]] = str(i+1)
        result = []
        for i in score:
            result.append(count[i])
        return result
# @lc code=end


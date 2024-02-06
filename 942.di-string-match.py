#
# @lc app=leetcode id=942 lang=python3
#
# [942] DI String Match
#

# @lc code=start
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ans = []
        mini = 0
        maxi = len(s)

        for c in s:
            if c == 'I':
                ans.append(mini)
                mini += 1
            else:
                ans.append(maxi)
                maxi -= 1

        return ans + [mini]
# @lc code=end


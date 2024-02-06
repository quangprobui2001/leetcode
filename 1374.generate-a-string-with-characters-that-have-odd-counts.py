#
# @lc app=leetcode id=1374 lang=python3
#
# [1374] Generate a String With Characters That Have Odd Counts
#

# @lc code=start
class Solution:
    def generateTheString(self, n: int) -> str:
        res = []
        if n % 2 == 0:
            for i in range(n-1):
                res.append('a')
            res.append('b')
        else:
            for i in range(n):
                res.append('a')
        return ''.join(res)

# @lc code=end


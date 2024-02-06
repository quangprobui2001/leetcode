#
# @lc app=leetcode id=598 lang=python
#
# [598] Range Addition II
#

# @lc code=start
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if ops==[]:
            return m*n
        return min(op[0] for op in ops)* min(op[1] for op in ops) 
# @lc code=end


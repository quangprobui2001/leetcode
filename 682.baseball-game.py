#
# @lc app=leetcode id=682 lang=python
#
# [682] Baseball Game
#

# @lc code=start
class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        history = []
        for op in operations:
            if op == 'C':
                history.pop()
            elif op == 'D':
                history.append(history[-1] * 2)
            elif op == '+':
                history.append(history[-1] + history[-2])
            else:
                history.append(int(op))
        return sum(history)
# @lc code=end


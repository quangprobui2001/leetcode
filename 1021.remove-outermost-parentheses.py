#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        index_remove=set()
        res=""
        for i, v in enumerate(S):
            if v == "(":
                stack.append(i)
            else:
                left_index = stack.pop()
                if not stack:
                    index_remove.add(left_index)
                    index_remove.add(i)
        for i, v in enumerate(S):
            if i not in index_remove:
                res+=v
        return res
# @lc code=end


#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for s in s:
            if s == '#' and s_stack:
                s_stack.pop()
                continue
            if s != '#': s_stack.append(s)
        for t in t:
            if t == '#' and t_stack:
                t_stack.pop()
                continue
            if t != '#': t_stack.append(t)
        return s_stack == t_stack
# @lc code=end


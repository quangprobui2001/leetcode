#
# @lc app=leetcode id=559 lang=python3
#
# [559] Maximum Depth of N-ary Tree
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: 
            return 0
        queue = collections.deque()
        depth = 1
        queue.append((root,depth))
        while queue:
            node, depth = queue.popleft()
            if node.children:
                for child in node.children:
                    queue.append((child,depth+1))
        return depth
# @lc code=end


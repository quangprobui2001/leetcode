#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        def dfs(node, left):
            if not node:
                return
            dfs(node.left, True)
            dfs(node.right, False)
            if not node.left and not node.right and left:
                self.total += node.val
        dfs(root, False)
        return self.total
# @lc code=end


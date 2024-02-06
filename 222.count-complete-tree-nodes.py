#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
       if not root:
           return 0
       def leftheight(node):
           if not node:
               return 0
           return 1 + leftheight(node.left)
       def rightheight(node):
           if not node:
               return 0
           return 1 + rightheight(node.right)
       l, r = leftheight(root), rightheight(root)
       if l > r:
           return 1 + self.countNodes(root.left) + self.countNodes(root.right)
       else:
           return (2**l) - 1 
# @lc code=end


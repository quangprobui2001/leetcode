#
# @lc app=leetcode id=783 lang=python
#
# [783] Minimum Distance Between BST Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.prev = None
        self.ans = float("inf")
        self.inorder(root)
        return self.ans

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        if self.prev is None:
            self.prev = root.val
        else:
            self.ans = min(self.ans, root.val - self.prev)
            self.prev = root.val
        self.inorder(root.right)
        
# @lc code=end


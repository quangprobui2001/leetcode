#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def search(node):
            if not node:
                return
            if low <= node.val <= high:
                self.ans += node.val
                search(node.left)
                search(node.right)
            elif node.val < low:
                search(node.right)
            elif node.val > high:
                search(node.left)

        self.ans = 0
        search(root)
        return self.ans 
# @lc code=end


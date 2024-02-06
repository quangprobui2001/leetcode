#
# @lc app=leetcode id=1379 lang=python3
#
# [1379] Find a Corresponding Node of a Binary Tree in a Clone of That Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original == target:
            return cloned
        if original.left:
            res = self.getTargetCopy(original.left, cloned.left, target)
            if res:
                return res
        if original.right:
            res = self.getTargetCopy(original.right, cloned.right, target)
            if res:
                return res
# @lc code=end


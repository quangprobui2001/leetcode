#
# @lc app=leetcode id=700 lang=python
#
# [700] Search in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        cur_node = root
        while cur_node:
            if cur_node.val == val:
                return cur_node
            elif cur_node.val < val:
                cur_node = cur_node.right
            else:
                cur_node = cur_node.left
# @lc code=end


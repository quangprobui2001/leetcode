#
# @lc app=leetcode id=671 lang=python
#
# [671] Second Minimum Node In a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        ans = float('inf')
        min_val = root.val
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            if min_val < curr.val < ans:
                ans = curr.val
            elif curr.val == min_val:
                stack.append(curr.left)
                stack.append(curr.right)
        return ans if ans < float('inf') else -1
        
# @lc code=end


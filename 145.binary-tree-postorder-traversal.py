#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            temp = stack[-1].right
            if temp:
                root = temp
            else:
                temp = stack.pop()
                res.append(temp.val)
                while stack and temp == stack[-1].right:
                    temp = stack.pop()
                    res.append(temp.val)
        return res
# @lc code=end


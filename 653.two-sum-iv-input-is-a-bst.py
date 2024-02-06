#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = set()
        s = [root]
        while s:
            cur = s.pop()
            if k - cur.val in nums:
                return True
            nums.add(cur.val)
            if cur.left:
                s.append(cur.left)
            if cur.right:
                s.append(cur.right)
        return False
# @lc code=end


#
# @lc app=leetcode id=637 lang=python
#
# [637] Average of Levels in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue = deque()
        queue.append((root, 1))
        ans = []
        counts = []
        total = 0
        level = 1
        count = 0
        while queue:
            curr, curr_level = queue.popleft()
            if level != curr_level:
                ans.append(float(total)/count)
                total, count = 0, 0
                level += 1
            total += curr.val
            count += 1
            if curr.left:
                queue.append((curr.left, curr_level + 1))
            if curr.right:
                queue.append((curr.right, curr_level + 1))
        if count != 0:
            ans.append(float(total)/count)
        return ans
# @lc code=end


#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        if not root:
            return result
        self.dfs(root, str(root.val), result)
        return result

    def dfs(self, node: TreeNode, current_path: str, result: List[str]):
        current_path += "->" + str(node.val)
        if not node.left and not node.right:
            result.append(current_path)
            return
        if node.left:
            self.dfs(node.left, current_path, result)
        if node.right:
            self.dfs(node.right, current_path, result)
        
# @lc code=end


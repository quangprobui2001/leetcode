#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#

# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxOfRight = -1
        for i in reversed(range(len(arr))):
            arr[i], maxOfRight = maxOfRight, max(maxOfRight, arr[i])
        return arr
# @lc code=end


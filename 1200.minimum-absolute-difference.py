#
# @lc app=leetcode id=1200 lang=python3
#
# [1200] Minimum Absolute Difference
#

# @lc code=start
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        m = float('inf')
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] < m:
                m = arr[i+1] - arr[i]
        
        res = []
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] == m:
                res.append((arr[i], arr[i+1]))
        return res 
# @lc code=end


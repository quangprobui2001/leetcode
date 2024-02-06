#
# @lc app=leetcode id=1089 lang=python3
#
# [1089] Duplicate Zeros
#

# @lc code=start
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)
        i = len(arr) - 1
        j = len(arr) + zeros - 1

        while i < j:
            if j < len(arr):
                arr[j] = arr[i]
            if arr[i] == 0:
                j -= 1
                if j < len(arr):
                    arr[j] = arr[i]
            i -= 1
            j -= 1
# @lc code=end


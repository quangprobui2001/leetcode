#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#

# @lc code=start
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans = []
        for i in range(len(num) - 1, -1, -1):
            k = k + num[i]
            ans.append(k % 10)
            k = k // 10
        while k:
            ans.append(k % 10)
            k = k // 10
        return ans[::-1]
# @lc code=end


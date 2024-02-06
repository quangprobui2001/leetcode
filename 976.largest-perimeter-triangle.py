#
# @lc app=leetcode id=976 lang=python
#
# [976] Largest Perimeter Triangle
#

# @lc code=start
class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A : List[int]
        :rtype: int
        """
        A.sort()
        for i in range(len(A) - 3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                return sum(A[i:i+3])
        else:
            return 0
        
# @lc code=end


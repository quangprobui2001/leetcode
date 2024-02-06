#
# @lc app=leetcode id=1013 lang=python
#
# [1013] Partition Array Into Three Parts With Equal Sum
#

# @lc code=start
class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        summ = sum(arr)
        if summ % 3 != 0:
            return False

        average = summ // 3
        partCount = 0
        partSum = 0

        for a in arr:
            partSum += a
            if partSum == average:
                partCount += 1
                partSum = 0

        return partCount >= 3
        
# @lc code=end


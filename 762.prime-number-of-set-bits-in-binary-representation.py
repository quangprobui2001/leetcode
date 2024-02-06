#
# @lc app=leetcode id=762 lang=python
#
# [762] Prime Number of Set Bits in Binary Representation
#

# @lc code=start
class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        count=0
        while left<=right:
            if str(bin(left)[2:]).count("1") in [2,3,5,7,11,13,17,19]: count+=1
            if str(bin(right)[2:]).count("1") in [2,3,5,7,11,13,17,19]:
                count+=1
                if left==right: count-=1
            left +=1
            right -=1
        return count
# @lc code=end


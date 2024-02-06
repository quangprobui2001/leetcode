#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        result = ""
        neg = num
        num = abs(num)
        if num == 0:
            return "0"
        while num > 0:
            remin = num % 7
            result += str(remin)
            num //= 7
        if neg < 0:
            return "-"+result[::-1]
        else:
            return result[::-1]
# @lc code=end


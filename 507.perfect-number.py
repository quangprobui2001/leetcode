#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        res = 0
        for i in range(1, int(num**0.5)+ 1):
            if num % i == 0:
                res += i
                if i * i != num:
                    res += num//i
        return res- num == num
# @lc code=end


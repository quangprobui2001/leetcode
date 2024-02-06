#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum, product = 0, 1
        while n:
          digit = n % 10
          sum += digit
          product *= digit
          n //= 10
        return product - sum
# @lc code=end


#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        output = []
        carry = 0
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        while p1 >= 0 or p2 >= 0:
            if p1 >= 0:
                v1 = ord(num1[p1]) - ord('0')
            else:
                v1 = 0
            if p2 >= 0:
                v2 = ord(num2[p2]) - ord('0')
            else:
                v2 = 0
            value = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) // 10
            output.append(value)
            p1 -= 1
            p2 -= 1
        if carry:
            output.append(carry)
        return "".join(str(i) for i in output[::-1])

# @lc code=end


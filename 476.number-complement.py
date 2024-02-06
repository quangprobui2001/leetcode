#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        binary = list("{:b}".format(num))
        for i in range(len(binary)):
            if binary[i] =="1":
                binary[i] = '0'
            else:
                binary[i] = "1"
        return int("".join(binary),base=2)
# @lc code=end


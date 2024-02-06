#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for x in range(1, n + 1):
            temp = ''
            if x % 3 == 0:
                temp += 'Fizz'
            if x % 5 == 0:
                temp += 'Buzz'
            if x % 3 != 0 and x % 5 != 0:
                temp += f'{x}'
            res.append(temp)
        return res
# @lc code=end


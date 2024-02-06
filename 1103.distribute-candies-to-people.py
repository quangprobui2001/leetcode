#
# @lc app=leetcode id=1103 lang=python3
#
# [1103] Distribute Candies to People
#

# @lc code=start
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        t = 0
        s = (1 + num_people) * num_people // 2
        cur = s
        while cur <= candies:
            t += 1
            cur += t * num_people * num_people + s
        res = [0] * num_people
        for i in range(num_people):
            res[i] = ((i+1) + ((i+1) + (t - 1) * num_people)) * t // 2
        candies -= sum(res)
        for i in range(num_people):
            tmp = min(candies, t * num_people + i + 1)
            res[i] += tmp
            candies -= tmp
        return res 
# @lc code=end


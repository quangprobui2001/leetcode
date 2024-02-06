#
# @lc app=leetcode id=492 lang=python3
#
# [492] Construct the Rectangle
#

# @lc code=start
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        mini = float(inf)
        ar = [area, 1]
        for i in range(1, int(area**0.5)+1):
            l = area / i
            if l == int(l) and l >= i and l - i < mini:
                ar[0]=int(l)
                ar[1] = i
                mini = l - i
        return ar
# @lc code=end


#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        length_row = len(grid)
        length_col = len(grid[0])
        p = 0
        connections = 0
        for x in range(0, length_row):
            for y in range(0, length_col):
                if grid[x][y] == 1:
                    p += 4
                    if x != 0 and grid[x-1][y] == 1:
                        connections += 1
                    if y !=0 and grid[x][y-1]==1 :
                        connections += 1
        return p -(connections * 2)
# @lc code=end


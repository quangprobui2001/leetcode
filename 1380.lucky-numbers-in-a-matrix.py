#
# @lc app=leetcode id=1380 lang=python3
#
# [1380] Lucky Numbers in a Matrix
#

# @lc code=start
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        flag = 0
        res = []
        for i in range(m):
            min_ = max_ = matrix[i][0]
            for j in range(n):
                if matrix[i][j] < min_:
                    flag = j
                    min_ = matrix[i][j]
            max_ = min_
            for x in range(m):
                if matrix[x][flag] > max_:
                    break
                elif x == m - 1:
                    res.append(max_)
        return res

        # solution two
        min_ = {min(rows) for rows in matrix}
        max_ = {max(columns) for columns in zip(*matrix)}  # zip(*) 对矩阵进行转置，即找出每一列中的最大值
        return list(min_ & max_)
# @lc code=end


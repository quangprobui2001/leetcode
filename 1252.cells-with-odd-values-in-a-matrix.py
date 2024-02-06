#
# @lc app=leetcode id=1252 lang=python3
#
# [1252] Cells with Odd Values in a Matrix
#

# @lc code=start
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [False] * m
        cols = [False] * n

        for r, c in indices:
            rows[r] ^= True
            cols[c] ^= True

        return sum(rows[i] ^ cols[j]
               for i in range(m)
               for j in range(n))
# @lc code=end


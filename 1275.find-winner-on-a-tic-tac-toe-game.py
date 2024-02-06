#
# @lc app=leetcode id=1275 lang=python3
#
# [1275] Find Winner on a Tic Tac Toe Game
#

# @lc code=start
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        row = [[0] * 3 for _ in range(2)]
        col = [[0] * 3 for _ in range(2)]
        diag1 = [0] * 2
        diag2 = [0] * 2
        i = 0

        for r, c in moves:
            row[i][r] += 1
            col[i][c] += 1
            diag1[i] += r == c
            diag2[i] += r + c == 2
            if 3 in (row[i][r], col[i][c], diag1[i], diag2[i]):
                return "A" if i == 0 else "B"
            i ^= 1

        return "Draw" if len(moves) == 9 else "Pending"
# @lc code=end


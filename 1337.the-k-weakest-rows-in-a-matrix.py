#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        power = []
        for r, row in enumerate(mat):
            tmp = 0
            for n in row:
                if n:
                    tmp += 1
                else:
                    break
            power.append((tmp, r))
        heapq.heapify(power)
        return [heapq.heappop(power)[1] for _ in range(k)]
# @lc code=end


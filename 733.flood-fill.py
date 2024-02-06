#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = [(sr, sc)]
        visited = {(sr, sc)}
        newcolor = image[sr][sc]
        while q:
            x, y = q.pop()
            image[x][y] = color
            for dirx, diry in directions:
                tx, ty = x + dirx, y + diry
                if 0 <= tx < m and 0 <= ty < n and image[tx][ty] == newcolor and (tx, ty) not in visited:
                    q.append((tx, ty))
                    visited.add((tx, ty))
        return image
# @lc code=end


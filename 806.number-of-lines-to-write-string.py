#
# @lc app=leetcode id=806 lang=python3
#
# [806] Number of Lines To Write String
#

# @lc code=start
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        numLines = 1
        runningWidth = 0

        for c in s:
            width = widths[ord(c) - ord('a')]
            if runningWidth + width <= 100:
                runningWidth += width
            else:
                numLines += 1
                runningWidth = width

        return [numLines, runningWidth]
# @lc code=end


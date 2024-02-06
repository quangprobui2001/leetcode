#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = bisect.bisect_right(range(len(letters)), target,
                            key=lambda m: letters[m])
        return letters[l % len(letters)]
# @lc code=end


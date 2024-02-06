#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        output = []
        for i in words:
            if re.match("^[qwertyuiop]+$", i.lower()) or re.match("^[asdfghjkl]+$", i.lower()) or re.match("^[zxcvbnm]+$", i.lower()):
                output.append(i)
        return output
# @lc code=end


#
# @lc app=leetcode id=1078 lang=python
#
# [1078] Occurrences After Bigram
#

# @lc code=start
class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        words = text.split()
        return [c for a, b, c in zip(words, words[1:], words[2:]) if a == first and b == second]
# @lc code=end


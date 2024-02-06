#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#

# @lc code=start
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        count = collections.Counter((A + ' ' + B).split())
        return [word for word, freq in count.items() if freq == 1]
# @lc code=end


#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        import collections
        counter = collections.Counter(list(s))
        for i in range(len(s)):
            if counter.get(s[i]) == 1:
                return i
        return -1
# @lc code=end


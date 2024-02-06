#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map = {}
        for c in magazine:
            if c not in map:
                map[c] = 1
            else:
                map[c] += 1
        for c in ransomNote:
            if c not in map or map[c] == 0:
                return False
            else:
                map[c] -= 1
        return True
# @lc code=end


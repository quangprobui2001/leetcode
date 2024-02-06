#
# @lc app=leetcode id=1370 lang=python3
#
# [1370] Increasing Decreasing String
#

# @lc code=start
class Solution:
    def sortString(self, s: str) -> str:
        cnt = Counter(s)
        cs = ascii_lowercase + ascii_lowercase[::-1]
        ans = []
        while len(ans) < len(s):
            for c in cs:
                if cnt[c]:
                    ans.append(c)
                    cnt[c] -= 1
        return "".join(ans)
# @lc code=end


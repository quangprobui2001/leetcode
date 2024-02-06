#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#

# @lc code=start
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ct = Counter(A[0])
        for w in A[1:]:
            tmp = Counter(w)
            for key in list(ct.keys()):
                if key not in tmp:
                    del ct[key]
                else:
                    ct[key] = min(ct[key], tmp[key])
        res = []
        for key in ct:
            res += [key] * ct[key]
        return res
# @lc code=end


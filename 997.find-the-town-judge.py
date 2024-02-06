#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ingress = defaultdict(set)
        egress =defaultdict(set)
        for p, q in trust:
            egress[p].add(q)
            ingress[q].add(p)
        for i in range(1, n+1):
            if len(egress[i]) == 0 and len(ingress[i]) == n - 1:
                return i
        return -1
# @lc code=end


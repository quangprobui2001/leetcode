#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        output = []
        for h in range (12):
            for m in range (60):
                temp = bin(h)+bin(m)
                if temp.count("1") == turnedOn:
                    time = '%d:%02d'% (h, m)
                    output.append(time)
        return output 
# @lc code=end


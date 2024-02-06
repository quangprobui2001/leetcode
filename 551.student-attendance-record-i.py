#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        abs = 0
        late = 0
        for x in s:
            if x == "A":
                abs += 1
                late = 0
            elif x == "L":
                late += 1
            else:
                late = 0
            if abs > 1 or late > 2:
                return False
        return True
# @lc code=end


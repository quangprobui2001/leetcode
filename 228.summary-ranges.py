#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        n = len(nums)
        if n == 0:
            return []
        start = nums[0]
        end = nums[0]
        for i in range(1, n):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end :
                    output.append(str(end))
                else:
                    output.append(str(start)+"->"+str(end))
                start = nums[i]
                end = nums[i]
        if start == end:
            output.append(str(end))
        else:
            output.append(str(start)+"->"+str(end))
        return output


        

# @lc code=end


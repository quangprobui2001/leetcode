#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count, index = {}, {}
        max_count = 0
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
                index[nums[i]] = [i, i]
            else:
                count[nums[i]] += 1
                index[nums[i]][1] = i
            max_count = max(max_count, count[nums[i]])
        
        min_len = len(nums)
        for k, v in count.items():
            if v == max_count:
                min_len = min(min_len, index[k][1] - index[k][0] + 1)
        return min_len 
# @lc code=end


#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0 
        
        while left <= right:

            mid = (right + left)//2
            guess = nums[mid]
            if guess == target:
                return mid
            elif guess > target:
                right = mid - 1
            elif guess < target:
                left = mid + 1
        return -1
# @lc code=end


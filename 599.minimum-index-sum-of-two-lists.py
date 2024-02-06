#
# @lc app=leetcode id=599 lang=python
#
# [599] Minimum Index Sum of Two Lists
#

# @lc code=start
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = {}
        for i in range(len(list1)):
            d[list1[i]] = i
        res, min_sum = [], float("inf")
        for i in range(len(list2)):
            curr = list2[i]
            if curr in d:
                curr_sum = i + d[curr]
                if curr_sum == min_sum:
                    res.append(curr)
                elif curr_sum < min_sum:
                    res, min_sum = [curr], curr_sum
        return res
# @lc code=end


#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        vowels = ['u', 'e', 'o', 'a', 'i', 'A', 'O', 'I', 'U', 'E']
        RV = list(s)
        while left < right:
            if RV[left] in vowels and RV[right] in vowels:
               RV[left], RV[right] = RV[right], RV[left]
               left += 1
               right -= 1
            elif not RV[left] in vowels:
               left += 1
            elif not RV[right] in vowels:
               right -= 1
        return "".join(RV)
# @lc code=end


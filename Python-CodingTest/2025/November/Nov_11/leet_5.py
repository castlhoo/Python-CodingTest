# 5. Longest Palindromic Substring
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        best_sol = [0, 0]
        best_len = 1
        s_len = len(s)
        l = -1
        r = s_len

        for i in range(len(s)):
            l = r = i

            while r < s_len - 1 and s[l] == s[r + 1]:
                r += 1

            while l > -1 and r < s_len and s[r] == s[l]:
                if r - l + 1 > best_len:
                    best_len = r - l + 1
                    best_sol = [l, r]
                l -= 1
                r += 1

        solution = ""
        for i in range(best_sol[0], best_sol[1] + 1):
            solution += s[i]

        return solution

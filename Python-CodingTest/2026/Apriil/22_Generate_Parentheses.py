# 22. Generate Parentheses
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        path = ""
        result = []
        open = 0
        close = 0

        def dfs(path, open, close):
            if len(path) == n * 2:
                result.append(path)
                return

            if open < n:
                dfs(path + "(", open + 1, close)
            if close < open:
                dfs(path + ")", open, close + 1)

        dfs(path, open, close)
        
        return result

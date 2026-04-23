# 17. Letter Combinations of a Phone Number
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 1 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []

        keypad = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }

        result = [""]

        for digit in digits:
            new_result = []

            for prev in result:
                for char in keypad[digit]:
                    new_result.append(prev + char)

            result = new_result
        
        return result
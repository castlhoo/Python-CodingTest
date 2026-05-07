# 47. Permutations II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

# Constraints:

# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        path = []
        used = [False for _ in range(len(nums))]

        def dfs(path):
            seen = set()

            if len(path) == len(nums):
                results.append(path[:])
            else:
                for i, num in enumerate(nums):
                    if used[i] is True:
                        continue
                    elif num in seen:
                        continue
                    else:
                        used[i] = True
                        path.append(num)
                        seen.add(num)
                        
                        dfs(path)

                        path.pop()
                        used[i] = False

        dfs(path)
        return results
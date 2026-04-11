# 200. Number of Islands
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        count = 0
        n = len(grid)
        m = len(grid[0])
        dirc = [(-1,0),(1,0),(0,-1),(0,1)]

        def bfs(x,y):
            queue = deque()
            queue.append((x,y))
            grid[x][y] = '0'

            while queue:
                x, y = queue.popleft()

                for dx, dy in dirc:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "1":
                        queue.append((nx, ny))
                        grid[nx][ny] = "0"
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    bfs(i,j)
                    count += 1
        
        return count
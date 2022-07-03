"""
Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
"""

from typing import List

def countIslands(grid: List[List[int]], i: int, j: int, count) -> int:
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0 or grid[i][j] == -1:
        return count 
    if grid[i][j] == 1:
        count += 1
        grid[i][j] = -1
    count = countIslands(grid, i - 1, j, count) # up
    count = countIslands(grid, i + 1, j, count) # down
    count = countIslands(grid, i, j - 1, count) # left
    count = countIslands(grid, i, j + 1, count) # right
    return count

def maxAreaOfIsland(grid: List[List[int]]) -> int:
    maxIslands = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            maxIslands = max(maxIslands, countIslands(grid, i, j, 0))
    return maxIslands

print(maxAreaOfIsland([
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]))
print(maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]))
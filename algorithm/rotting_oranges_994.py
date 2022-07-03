"""
Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1

Example 3:
Input: grid = [[0,2]]
Output: 0
"""
from typing import List
from collections import deque

def fourDirections(grid: List[List[int]], i: int, j: int, q) -> int:
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0 or grid[i][j] == 2:
        return 0
    q.append([i, j])
    return 1

def orangesRotting(grid: List[List[int]]) -> int:
    q = deque()
    orangeCount = 0
    # Count the number of oranges and append the rotten oranges to the queue
    for i in range(len(grid)):
        for j, entry in enumerate(grid[i]):
            if entry > 0:
                orangeCount += 1
            if entry == 2:
                q.append([i, j])
            
    # dequeue until the queue is empty
    rottenCount = len(q)
    minute = 0
    while len(q):
        for _ in range(len(q)):
            i, j = q.popleft() # Pop a rotten orange
            rottenCount += fourDirections(grid, i + 1, j, q) # up
            rottenCount += fourDirections(grid, i - 1, j, q) # down
            rottenCount += fourDirections(grid, i, j + 1, q) # left
            rottenCount += fourDirections(grid, i, j - 1, q) # right 
        minute += 1
    print(minute)


orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
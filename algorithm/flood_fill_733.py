"""
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.
"""
from typing import List

# def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#     if (sr < 0 or sr >= len(image)) or (sc < 0 or sc >= len(image)) or image[sr][sc] != 1:
#         return
#     image[sr][sc] = color 
#     # Left
#     floodFill(image, sr, sc - 1, color)
#     # right
#     floodFill(image, sr, sc + 1, color)
#     # up
#     floodFill(image, sr - 1, sc, color)
#     # down
#     floodFill(image, sr + 1, sc, color)

#     return image

# def dfs(image, sr, sc, color, start):
#     if (sr < 0 or sr >= len(image)) or (sc < 0 or sc >= len(image)):
#         return
#     if (image[sr][sc] != start):
#         return
#     image[sr][sc] = color 
#     # Left
#     dfs(image, sr, sc - 1, color, start)
#     # up
#     dfs(image, sr - 1, sc, color, start)
#     # right
#     dfs(image, sr, sc + 1, color, start)
#     # down
#     dfs(image, sr + 1, sc, color, start)

# def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#     if image[sr][sc] == color:
#         return image
#     dfs(image, sr, sc, color, image[sr][sc])
#     return image

def dfs(image, sr, sc, color, start):
    if (sr < 0 or sr >= len(image)) or (sc < 0 or sc >= len(image[0])):
        return
    if (image[sr][sc] != start):
        return
    image[sr][sc] = color 
    dfs(image, sr - 1, sc, color, start) # up
    dfs(image, sr + 1, sc, color, start) # down
    dfs(image, sr, sc - 1, color, start) # left
    dfs(image, sr, sc + 1, color, start) # right

def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    if image[sr][sc] == color:
        return image
    dfs(image, sr, sc, color, image[sr][sc])
    return image


result = floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
# result = floodFill([[0,0,0],[0,0,0]], 0, 0, 0)
# result = floodFill([[0,0,0],[0,0,0]], 1, 0, 2)
for row in result:
    print(row)
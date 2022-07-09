"""
Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []
"""
from typing import List

class Node:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def rightSideView(root: Node) -> List[int]:
    res = []
    def dfs(root, height):
        if not root: return 
        if height >= len(res):
            res.append(root.val)
        dfs(root.right, height + 1)
        dfs(root.left, height + 1)

    dfs(root, 0) 
    return res

root = Node(1, Node(2, None, Node(5)), Node(3, None, Node(4)))
root = Node(1, Node(2, None, Node(5, None, Node(6))), Node(3, None, Node(4)))
root = Node(1, Node(2, Node(7, Node(8, Node(9))), Node(5, None, Node(6))), Node(3, None, Node(4)))
# root = Node(1, None, Node(3))
print(rightSideView(root))
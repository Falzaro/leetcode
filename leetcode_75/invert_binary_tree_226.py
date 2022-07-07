"""
Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
"""

import sys
sys.path.append(".")
from binary_tree.bfs_traversal import bfs
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: Node) -> Node:
    if not root:
        return root
    invertTree(root.left)
    invertTree(root.right)
    root.left, root.right = root.right, root.left
    return root

root = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(6), Node(9)))
root = Node(2, Node(1), Node(3))
root = Node(4, Node(2, Node(1)), Node(7, None, Node(9)))
root = invertTree(root)
print(bfs(root))

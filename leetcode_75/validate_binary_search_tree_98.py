"""
Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

notes
- Didn't know that we can use negative/positive infinity
"""
import sys
sys.path.append(".")
from binary_tree.bfs_traversal import bfs

class Node:
    def __init__(self, val=0, left=None, right=None) -> bool:
        self.val = val
        self.left = left
        self.right = right

def valid(root, lower, upper):
    if not root:
        return True
    if not (lower < root.val < upper):
        return False
    return (valid(root.left, lower, root.val) 
            and valid(root.right, root.val, upper))

def isValidBST(root: Node) -> bool:
    return valid(root, float("-inf"), float("inf"))

# Ex: 1
root = Node(2, Node(1), Node(3))
print(isValidBST(root))

# Ex: 2
root = Node(5, Node(1), Node(4, Node(3), Node(6)))
print(isValidBST(root))

root = Node(1, None, Node(1))
print(isValidBST(root))

""" Other test cases """
# [1, null, 1]
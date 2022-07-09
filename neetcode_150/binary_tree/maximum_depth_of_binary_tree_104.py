"""
Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
"""

class Node:
    def __init__(self, val=0, left=None, right=None) -> bool:
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Node) -> int:
    if not root: return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

root = Node(3, Node(9), Node(20, Node(15), Node(7)))
print(maxDepth(root)) # -> 3
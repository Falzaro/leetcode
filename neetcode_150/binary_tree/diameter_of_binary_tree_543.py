"""
Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1

Notes:
The diameter of a tree is the length of the longest path between any two nodes in a tree.

tips:
1. use a global variable to store the max value
2. use a helper function to calculate the max value
3. The height can be obtained by the returned value of left subtree and right subtree
"""

class Node:
    def __init__(self, val=0, left=None, right=None) -> bool:
        self.val = val
        self.left = left
        self.right = right
    

def diameterOfBinaryTree(root: Node) -> int:
    """ time complexity: O(n), space complexity: O(n) """
    res = 0
    def treeHeight(root):
        if not root: return 0
        left = treeHeight(root.left)
        right = treeHeight(root.right)
        nonlocal res
        res = max(res, left + right)
        return max(left, right) + 1
    treeHeight(root)
    return res


root = Node(1, Node(2, Node(4), Node(5)), Node(3))
# root = Node(1, Node(2))
print(diameterOfBinaryTree(root)) # 3
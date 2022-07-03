from collections import deque

import sys
sys.path.append(".")
from binary_tree.binary_tree import TreeNode

"""
Input: root1 = [1, 3, 2, 5], root2 = [2, 1, 3, null, 4, null, 7]
"""
def mergeTrees(root1: TreeNode, root2: TreeNode) -> TreeNode:
    if not root1: return root2
    if not root2: return root1
    root1.val += root2.val
    root1.left = mergeTrees(root1.left, root2.left)
    root1.right = mergeTrees(root1.right, root2.right)
    return root1


root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

mergeTrees(root1, root2)
"""
Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2
"""
import sys
sys.path.append('.')
from binary_tree.bfs_traversal import bfs

class Node:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def findAncestor(root, d, ancestor):
    if not root: return None
    if root.val in d:
        if len(d) == 1:
            return ancestor
        ancestor = root
        d.remove(root.val)
    ancestor = findAncestor(root.left, d, ancestor)
    ancestor = findAncestor(root.right, d, ancestor)
    if ancestor: return ancestor
    if root.left in d or root.right in d:
        return root

def lowestCommonAncestor(root: 'Node', p: 'Node', q: 'Node') -> 'Node':
    return findAncestor(root, set([p.val, q.val]), None)


root = Node(6, Node(2, Node(0), Node(4, Node(3), Node(5))), Node(8, Node(7), Node(9)))
print(lowestCommonAncestor(root, Node(2), Node(8)).val)

# root = Node(6, Node(2, Node(0), Node(4, Node(3), Node(5))), Node(8, Node(7), Node(9)))
# print(lowestCommonAncestor(root, Node(2), Node(4)).val)

# root = Node(2, None, Node(1))
# print(lowestCommonAncestor(root, Node(2), Node(2)).val)
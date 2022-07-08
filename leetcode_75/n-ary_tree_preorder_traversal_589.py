"""
Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000.
"""

from typing import List
class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

def preorder(root: 'Node') -> List[int]:
    if not root: return []
    q = [root]
    res = []
    while len(q):
        node = q.pop()
        res.append(node.val)
        for child in reversed(node.children):
            q.append(child)
    return res


root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
print(preorder(root))

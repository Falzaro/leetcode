"""
Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]

Example 2:
Input: root = []
Output: []
"""

"""
Post completion notes:
- We can return the root node after popping the last call stack
- Initializing an entire tree can be done with just one Node constructor
"""

from collections import deque
import sys
sys.path.append('../')

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# def connect(root: Node) -> Node:
#     if not root:
#         return None
#     if not root.left and not root.right:
#         return root
#     q = deque([root.left, root.right])
#     while len(q):
#         size = len(q)
#         while size > 0:
#             left = q.popleft()
#             right = q.popleft()
#             left.next = right
#             size -= 2
#             if left.left:
#                 q.append(left.left)
#                 q.append(left.right)
#                 q.append(right.left)
#                 q.append(right.right)
#             if size > 0:
#                 right.next = q[0]
#     return root

def connect(root: Node) -> Node:
    if not root: return None
    if not root.left: return root
    root.left.next = root.right
    connect(root.left)
    connect(root.right)
    if root.next:
        root.right = root.next.left
    return root

# root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(2)
root = Node(0)
root = connect(root)
print(root.val)
# print(root.left.val)
# print(root.right.val)
# print(root.left.next.val)
# print(root.left.right.next.val)
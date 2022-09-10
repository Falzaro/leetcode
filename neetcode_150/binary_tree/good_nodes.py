"""
Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.
"""

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def goodNodes(root) -> int:
    def dfs(root, maxVal, good):
        if not root: return good
        if root.val >= maxVal:
            good += 1
            maxVal = root.val
        good = dfs(root.left, maxVal, good)
        return dfs(root.right, maxVal, good) 
        
    return dfs(root, root.val, 0)

root = Node(3, Node(1, Node(3), None), Node(4, Node(1), Node(5)))
print(goodNodes(root))
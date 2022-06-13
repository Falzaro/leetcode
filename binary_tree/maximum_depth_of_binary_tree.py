from binary_tree import initialize_tree, TreeNode
from bfs_traversal import levelOrderArraysNums 

# Initialize the binary tree
# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

root = TreeNode(1)
root.right = TreeNode(2)

# def dfs(node):

def maxDepth(root):
    if not root:
        return 0
    return max(maxDepth(root.left) + 1, maxDepth(root.right) + 1)


result = maxDepth(root)
print(result)
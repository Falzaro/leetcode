class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def addNode(root, num):
    if not root: return TreeNode(num)
    if not num: return root
    if num > root.val:
        if not root.right:
            root.right = TreeNode(num)
        else:
            addNode(root.right, num)
    else:
        if not root.left:
            root.left = TreeNode(num)
        else:
            addNode(root.left, num)
    return root

def removeNode(root, num):
    pass

def initialize_tree(nums):
    root = None
    for num in nums:
        root = addNode(root, num)
    return root





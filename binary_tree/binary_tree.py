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

def initialize_tree(nums):
    root = None
    for num in nums:
        root = addNode(root, num)
    return root

def pre_order(root):
    if root == None:
        return
    print(root.val, end=" ")
    pre_order(root.left)
    pre_order(root.right)

def in_order(root):
    if root == None:
        return
    in_order(root.left)
    print(root.val, end=" ")
    in_order(root.right)

def post_order(root):
    if root == None:
        return
    post_order(root.left) 
    post_order(root.right)
    print(root.val, end=" ")

# root = initialize_tree([50, 76, 21, 4, 32, 64, 15, 52, 14, 100, 83, 2, 3, 70, 87, 80])
root = initialize_tree([1,None,2,3])
# root = initialize_tree([1])
result = pre_order(root)
print(result)
# in_order(root)
# post_order(root)



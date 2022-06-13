from binary_tree import initialize_tree

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
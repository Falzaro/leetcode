# from binary_tree import initialize_tree
from collections import deque

def levelOrder(root):
    queue = []
    queue.append(root)
    while len(queue) != 0:
        node = queue.pop(0)
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def levelOrderArrays(root):
    result = []
    curLevel = [root]
    while len(curLevel) != 0:
        newLevel = []
        result.append(curLevel)
        for node in curLevel:
            if node.left:
                newLevel.append(node.left)
            if node.right:
                newLevel.append(node.right)
        curLevel = newLevel
    print(result)

def bfs(root):
    if not root: return res
    res = []
    q = deque([root])
    while len(q):
        size = len(q)
        curLevel = []
        for _ in range(size):
            node = q.popleft()
            curLevel.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(curLevel)
    return res
            
def levelOrderArraysNums(root):
    result = []
    if not root: return result
    curLevel = [root]
    while len(curLevel) != 0:
        newLevel = []
        nums = []
        for node in curLevel:
            nums.append(node.val)
            if node.left:
                newLevel.append(node.left)
            if node.right:
                newLevel.append(node.right)
        result.append(nums)
        curLevel = newLevel
    print(result)

# root = initialize_tree([5, 3, 9, 4, 2, 8, 10])
# levelOrder(root)
# levelOrderArrays(root)
# print(bfs(root))

# [[5], [3, 9], [2, 4, 8, 10]]



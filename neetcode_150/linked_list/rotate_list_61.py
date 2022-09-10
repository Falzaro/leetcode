"""
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    if not head: return None
    runner = head
    cur = head
    size = 0
    while cur:
        cur = cur.next
        size += 1
    k = k % size
    while k:
        runner = runner.next
        k -= 1
    cur = head
    while runner.next:
        runner = runner.next
        cur = cur.next
    runner.next = head
    head = cur.next
    cur.next = None
    return head
    

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(rotateRight(head, 2).val)
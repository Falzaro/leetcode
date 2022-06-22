"""
Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
"""
from linked_list import initialize_list, outputNodes

def reverseList(head):
    cur = head 
    prev = None
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev

head = initialize_list([1, 2, 3, 4, 5])
outputNodes(head)
# print("---------")
# head = reverseList(head)
# outputNodes(head)
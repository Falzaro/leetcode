"""
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []
"""
from typing import Optional
import sys
sys.path.append(".")
from linked_list.linked_list import ListNode, outputNodes, initialize_list

# def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
#     cur = runner = head
#     count = 1
#     while runner.next:
#         count += 1
#         runner = runner.next
#     if count == n:
#         return cur.next
#     index = 1
#     while cur.next:
#         if index == count - n:
#             cur.next = cur.next.next
#             return head
#         cur = cur.next
#         index += 1

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    cur = runner = head
    while n > 0:
        runner = runner.next
        n -= 1
    if not runner:
        return head.next
    while runner.next:
        runner = runner.next
        cur = cur.next
    cur.next = cur.next.next
    return head

head = initialize_list([1, 2, 3, 4, 5])
outputNodes(removeNthFromEnd(head, 2))
print()
head = initialize_list([1, 2])
outputNodes(removeNthFromEnd(head, 1))
print()
head = initialize_list([1, 2])
outputNodes(removeNthFromEnd(head, 2))
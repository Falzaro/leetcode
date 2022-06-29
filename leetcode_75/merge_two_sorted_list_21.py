"""
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""

from typing import Optional
import sys
sys.path.append(".")

from linked_list.linked_list import ListNode, initialize_list, outputNodes

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = cur = ListNode()
    while list1 and list2:
        if list1.val <= list2.val:
            cur.next = list1
            cur = cur.next
            list1 = list1.next
        else:
            cur.next = list2
            cur = cur.next
            list2 = list2.next
    if list1:
        cur.next = list1
    if list2:
        cur.next = list2
    outputNodes(dummy.next)

head1 = initialize_list([1, 2, 4])
head2 = initialize_list([1, 3, 4])
# head = mergeTwoLists(head1, head2)

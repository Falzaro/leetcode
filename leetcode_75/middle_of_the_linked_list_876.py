"""
Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
"""
from typing import Optional

import sys
sys.path.append('.')
from linked_list.linked_list import ListNode, outputNodes, initialize_list

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while True:
        if not fast.next:
            return slow
        if not fast.next.next:
            return slow.next
        slow = slow.next
        fast = fast.next.next


head = initialize_list([1, 2, 3, 4, 5])
outputNodes(middleNode(head))
print()
head = initialize_list([1, 2, 3, 4, 5, 6])
outputNodes(middleNode(head))

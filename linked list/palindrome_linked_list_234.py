"""
Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
"""
from linked_list import addNodes, outputNodes

def isPalindrome(head):
    slow = fast = head
    # Get the middle node of the linked list
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # reverse slow linked list
    cur = slow
    prev = None
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    # Compare the two linked lists and see if they have the same node values
    while prev:
        if head.val != prev.val:
            return False
        head, prev = head.next, prev.next
    return True


head = addNodes([1])
result = isPalindrome(head)
print(result)
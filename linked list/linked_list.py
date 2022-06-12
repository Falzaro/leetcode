class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def initialize_list(nums):
    head = None
    for num in nums:
        newNode = ListNode(num)
        if head == None:
            head = newNode
        else:
            cur = head
            while cur.next:
                cur = cur.next
            cur.next = newNode
    return head

def outputNodes(head):
    if head == None:
        return
    print(head.val, end=" ")
    return outputNodes(head.next)
    

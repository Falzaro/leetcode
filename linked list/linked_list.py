class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def addNodes(nums):
    cur = head = ListNode(nums[0])
    for num in nums[1:]:
        cur.next = ListNode(num)
        cur = cur.next
    return head

def outputNodes(head):
    if head == None:
        return
    print(head.val)
    return outputNodes(head.next)
    

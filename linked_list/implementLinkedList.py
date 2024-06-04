class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#         self.next = next

l1 = [1,2,3,4,5,6,7]
ll = ListNode()

curr = head = ListNode()
for i in range(len(l1) - 1):
    curr.val = l1[i]
    curr.next = ListNode(l1[i+1])



while curr:
    print(curr.val)
    curr = curr.next
    

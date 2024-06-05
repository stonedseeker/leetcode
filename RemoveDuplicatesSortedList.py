from typing import Optional


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None:
            return head

        curr = head
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
    
            else:
                curr = curr.next

       
        return head


head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, None)))))
head = ListNode(1, ListNode(1, ListNode(1, None)))

curr = Solution().duplicates(head)

while curr:
    print(curr.val)
    curr = curr.next

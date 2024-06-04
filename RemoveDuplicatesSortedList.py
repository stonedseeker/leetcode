from typing import Optional


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr.next :
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            
            curr = curr.next

        return head


head = ListNode(1, ListNode(1, ListNode(2, None)))

curr = Solution().duplicates(head)

while curr:
    print(curr.val)
    curr = curr.next

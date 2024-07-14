# Definition for singly-linked list.

from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, headk

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None

        while slow:
            
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp 

        dummy = res = ListNode(0, None)

        curr = head
        while curr and prev:
            dummy.next = ListNode(curr.val)
            dummy = dummy.next
            dummy.next = ListNode(prev.val)
            dummy = dummy.next
            curr = curr.next
            prev = prev.next
        return res.next

node1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))

res = Solution().reorderList(node1)

curr = res
while curr:
    print(curr.val)
    curr = curr.next

        

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = head
        curr = head
        lLen = 0
        while curr != None:
            curr = curr.next
            lLen += 1

        k = lLen // k

        res = dummy

    def revList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None
        
        while head:
            temp = head.next
            head.next = tail
            tail = head
            head = temp
        
        temp = tail
        return tail


nomde = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))

temp = Solution().revList(nomde)
while temp != None:
    print(temp.val)
    temp = temp.next



 

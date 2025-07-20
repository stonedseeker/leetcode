from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(head, tail):
            if not head:
                return tail
            temp = head.next
            head.next = tail

            return reverse(temp, head)

        return reverse(head, None)

head = Solution().reverseList(ListNode(1,ListNode(2,ListNode(3,ListNode(4, ListNode(5, None))))))

while head:
    print(head.val)
    head = head.next



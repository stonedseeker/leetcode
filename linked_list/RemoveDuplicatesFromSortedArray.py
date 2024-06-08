from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if head == None or head.next == None:
            return head

        dummy = ListNode(0, head)

        curr = dummy
        while curr:
            if curr.next and curr.next.next and curr.next.val == curr.next.next.val:
                temp = curr.next.val 
                while (curr.next and curr.next.val == temp):
                    curr.next = curr.next.next
            else:
                curr = curr.next
        
        return dummy.next
node = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode (3, ListNode(4, ListNode(4, ListNode(5, None))))))))
node = Solution().deleteDuplicates(node)
curr = node
while curr:
    print(curr.val)
    curr = curr.next


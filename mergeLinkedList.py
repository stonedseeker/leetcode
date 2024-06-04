from typing_extensions import LiteralString


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        
        while l1 or l2:
            if l1.val < l2.val:
                l1.next = self.merge(l1.next, l2)
                return l1
            else:
                l2.next = self.merge(l1, l2.next)
                return l2

        curr = l1
        while curr:
            print(curr.val)
            curr = curr.next
l1,n2,n3,n4 = ListNode(1), ListNode(3), ListNode(5), ListNode(7)
l1 = ListNode(1,n2)
n2 = ListNode(3, n3)
n3 = ListNode(5, n4)

l5,l6,l7,l8 = ListNode(2), ListNode(4), ListNode(6), ListNode(8)
l5 = ListNode(2, l6)
l6 = ListNode(4, l7)
l7 = ListNode(6, l8)




print(Solution().merge(l1,l5))


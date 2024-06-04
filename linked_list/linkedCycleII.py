from typing import Optional

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def detectCycle( head: Optional[ListNode]) -> Optional[ListNode]:

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                break
        
        length = 0

        while slow.next != fast:
            slow = slow.next
            length += 1

        print(length)

        fast = head

        while length != 0:
            fast = fast.next
            length -= 1  # decrement the length in each iteration

        return fast

a = ListNode(3)
b = ListNode(2)

c = ListNode(0)

d = ListNode(-4)

a.next = b
b.next = c
c.next = d
d.next = a

print(detectCycle(a).val)

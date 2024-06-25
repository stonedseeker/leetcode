class Solution:
    def countNodes(self, head):
        curr = head
        count = 0
        while curr:
            curr = curr.next
            count += 1

        return count
class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

node = ListNode(1, ListNode(2, ListNode(3, None)))
print(Solution().countNodes(node))
     

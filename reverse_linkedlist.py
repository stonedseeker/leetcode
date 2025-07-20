from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = None


class Solution:
    def reverseList(self, head:Optional[ListNode]) -> Optional[ListNode]:
        
        tail = dummy = head
    
    '''
        now what to do here, we have to reverse a List
        now how do we do that?
        this is a ListNode

        1 -> 2 -> 3
        
        take an empty list tail
        
        point tail to head 
        
        point head to tail.next

        

    '''
        dummy = tail = ListNode()
        
        while dummy:
            
            temp = head.next 
            head.next = tail
            tail = head
            dummy = dummy.next
    


        return tail


head = ListNode(1,ListNode(2, ListNode(3, ListNode(4, None))))
tail = Solution().reverseList(head)

while head:
    print(head.val)



from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        
        while(head != None):
            nums.append(head.val)
            head = head.next

        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] != nums[r]: return False
            l += 1
            r -= 1
        return True


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4

# Create an instance of the Solution class

# Test the isPalindrome method
result = Solution().isPalindrome(node1)
print(result)

# Exit Python
exit()


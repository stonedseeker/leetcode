
from typing import List, Optional
from collections import deque

class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val 
        self.next = next



class TreeNode:
    def __init__(self, val, left, right) -> None:
        self.val = val
        self.left= left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> Optional[ListNode]:
        
        def dfs(root, q):
            if root:
                q.append(root)
                dfs(root.left, q)
                dfs(root.right, q)
        

        q = deque()
        dfs(root, q)

        head = node = ListNode(0, None)

        while q:
            
            node.next = ListNode(q.popleft().val)
            node = node.next

        return head.next


    

        



node3 = TreeNode(3, None, None)
node4 = TreeNode(4, None, None)
node2 = TreeNode(2, node3, node4)
node6 = TreeNode(6, None, None)
node5 = TreeNode(5, None, node6)
node1 = TreeNode(1, node2, node5)


curr =  Solution().flatten(node1)

while curr:
    print(curr.val)
    curr = curr.next

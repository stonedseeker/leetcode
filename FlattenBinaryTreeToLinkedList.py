
from typing import Optional
from collections import deque

class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        this.val = val 
        this.next = next



class TreeNode:
    def __init__(self, val, left, right) -> None:
        self.val = val
        self.left= left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        def dfs(root, q):
            if root:
                dfs(root.left, q)
                dfs(root.right, q)
                q.append(root)

        q = deque()
        dfs(root, q)

        while q:
            print(q.popleft().val)


    

        



node3 = TreeNode(3, None, None)
node4 = TreeNode(4, None, None)
node2 = TreeNode(2, node3, node4)
node6 = TreeNode(6, None, None)
node5 = TreeNode(5, None, node6)
node1 = TreeNode(1, node2, node5)


print(Solution().flatten(node1))

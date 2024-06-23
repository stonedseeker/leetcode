# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count, self.res = 0, 0
    
        def dfs(root, k):
            if not root or self.count >= k:
                return
            dfs(root.left, k)

            self.count += 1
            if self.count == k:
                self.res = root.val
                return 
            dfs(root.right, k)
        dfs(root, k)
        return self.res

node2 = TreeNode(2, None, None)
node4 = TreeNode(4, None, None)
node1 = TreeNode(1, None, node2)
node3 = TreeNode(3, node1, node4)


print(Solution().kthSmallest(node3, 1))

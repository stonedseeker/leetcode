from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            left = max(0, left)
            left = max(0, right) 
            res[0] = max(left + right + root.val, res[0])

            return root.val + max(left, right)  

        dfs(root)
        return res[0]


node3 = TreeNode(3, None,None)
node2 = TreeNode(2, None,None)
node1 = TreeNode(1, node2, node3)

print(Solution().maxPathSum(node1))


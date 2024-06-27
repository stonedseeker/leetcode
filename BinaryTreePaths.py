from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res = []

        def dfs(root, memo = []):
            if not root:
                self.res.append(memo)
                return
            memo.append(root.val)
            dfs(root.left, memo)

            dfs(root.right, memo)
            
        
        dfs(root, [])
        
        return self.res

node5 = TreeNode(5, None, None)
node2 = TreeNode(2, None, node5)
node3 = TreeNode(3, None, None)
node1 = TreeNode(1, node2, node3)

print(Solution().binaryTreePaths(node1))

